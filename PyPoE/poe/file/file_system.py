"""
Overview
===============================================================================

+----------+------------------------------------------------------------------+
| Path     | PyPoE/poe/file/file_system.py                                    |
+----------+------------------------------------------------------------------+
| Version  | 1.0.0a0                                                          |
+----------+------------------------------------------------------------------+
| Revision | $Id$                  |
+----------+------------------------------------------------------------------+
| Author   | Omega_K2                                                         |
+----------+------------------------------------------------------------------+

Description
===============================================================================



Agreement
===============================================================================

See PyPoE/LICENSE

Documentation
===============================================================================

Classes
-------------------------------------------------------------------------------

.. autoclass: FileSystem

.. autoclass: FileSystemNode
"""

# =============================================================================
# Imports
# =============================================================================

# Python
import json
import os
from typing import Union

# 3rd-party
import brotli
import requests

# self
from PyPoE.poe.file.shared import FILE_SYSTEM_TYPES, AbstractFileSystemNode
from PyPoE.poe.file.ggpk import GGPKFile
from PyPoE.poe.file.bundle import Index
from PyPoE.poe.file.shared import ParserError

# =============================================================================
# Globals
# =============================================================================

__all__ = ['FileSystem']

# =============================================================================
# Classes
# =============================================================================


class InyaRemote:
    remote_name: str
    remote_build: str

    def _match_servers(self, kind):
        servers = dict(map(lambda x: (x['name'], x), self.servers['servers'][kind]))
        for server in servers.values():
            if 'required_tags' not in server:
                server['tag_rank'] = 0
            else:
                unmatched = set(server['required_tags']) - self.tags
                if len(unmatched) > 0:
                    server['tag_rank'] = None
                else:
                    server['tag_rank'] = len(server['required_tags'])

        return list(map(lambda x: x[1],
                    sorted(filter(lambda x: x[1]['tag_rank'] is not None, servers.items()),
                           key=lambda x: x[1]['tag_rank'],
                           reverse=True)))

    def __init__(self, remote_path):
        parts = remote_path.split(':')
        self.remote_name = parts[1]
        self.remote_build = parts[2]

        self.tags = set(['zao-lan'])
        self.servers = requests.get('https://zao.se/poe-meta/catalog.json').json()

        self.data_server = self._match_servers('data')[0]['url']
        self.index_server = self._match_servers('index')[0]['url']
        self.meta_server = self._match_servers('meta')[0]['url']

        build_url = f'{self.meta_server}/build/{self.remote_build}.json'
        build = requests.get(build_url).json()
        data_manifest = build['manifests']['238961']
        index_url = f'{self.index_server}/index/{data_manifest}.json'
        self.index = requests.get(index_url).json()
        self.paths = {x["path"]: x for x in self.index['files']}

    def get_file(self, path):
        if path not in self.paths:
            raise FileNotFoundError()
        rec = self.paths[path]
        try:
            hash = rec["hash"]
            data_url = f'{self.data_server}/data/{hash[:3]}/{hash}.bin'
            return requests.get(data_url).content
        except requests.exceptions.RequestException:
            raise FileNotFoundError()


class FileSystemNode(AbstractFileSystemNode):
    _REPR_ARGUMENTS_IGNORE = {'parent'}

    __slots__ = ['file_system'] + AbstractFileSystemNode.__slots__

    def __init__(self,
                 *args,
                 parent: 'FileSystemNode',
                 file_system_type: FILE_SYSTEM_TYPES,
                 is_file: bool,
                 file_system: 'FileSystem',
                 name: str,
                 **kwargs):

        super().__init__(
            *args,
            parent=parent,
            file_system_type=file_system_type,
            is_file=is_file,
            **kwargs)

        self.file_system: 'FileSystem' = file_system
        self._name: str = name

    @property
    def data(self) -> bytes:
        if self.is_file:
            return self.file_system.get_file(self.get_path())
        else:
            raise ValueError

    @property
    def name(self) -> str:
        return self._name


class FileSystem:
    """
    The FileSystem class is used to simplify accessing files from the game via
    a single call rather then checking disk, ggpk or bundles separately.

    Upon initialization of the class, the corresponding Index bundle and GGPK
    will be automatically read if present.

    Further decompression of bundles or reading of data will be only be done
    when the get_file method is called.
    """
    def __init__(self, root_path: str):
        """
        Parameters
        ----------
        root_path
            The root game directory path (where PathOfExile.exe is located)
        """
        self.directory: Union[FileSystemNode, None] = None

        self.root_path: str = root_path
        self.ggpk: Union[GGPKFile, None] = None

        if root_path.startswith('remote:'):
            self.remote = InyaRemote(self.root_path)
            return

        ggpk_path = os.path.join(root_path, 'Content.ggpk')
        if os.path.exists(os.path.join(root_path, 'Content.ggpk')):
            self.ggpk = GGPKFile()
            self.ggpk.read(ggpk_path)
            self.ggpk.directory_build()

        self.index: Union[Index, None] = Index()
        try:
            if self.ggpk:
                self.index.read(self.ggpk[self.index.PATH].record.extract())
            else:
                self.index.read(os.path.join(root_path, self.index.PATH))
        except FileNotFoundError:
            self.index = None

    def get_file(self, path: str) -> bytes:
        """
        Retrieves a file contents as binary data via the given path (relative
        to the root directory)

        Parameters
        ----------
        path
            The path relative to the root game directory (i.e. root_path)

        Returns
        -------
            The unbuffered binary file data in bytes
        """
        if self.remote:
            return self.remote.get_file(path)

        if self.index:
            try:
                fr = self.index.get_file_record(path)
            except FileNotFoundError:
                pass
            else:
                if self.ggpk:
                    fr.bundle.read(
                        self.ggpk[fr.bundle.ggpk_path].record.extract()
                    )
                else:
                    fr.bundle.read(os.path.join(
                        self.root_path, fr.bundle.ggpk_path))
                return fr.get_file()

        # If the file is in the index, this section can't be reached
        if self.ggpk:
            try:
                return self.ggpk[path].record.extract()
            except FileNotFoundError:
                pass

        # If no GGPK is loaded or the file isn't within the GGPK, lastly the
        # root directory is tried
        try:
            with open(os.path.join(self.root_path, path), 'rb') as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(
                'Specified file can not be found in the Index, content.ggpk '
                'or disk')

    def extract_dds(self, data: bytes) -> bytes:
        """
        Attempts to extract a .dds from the given data bytes.

        .dds files in the content.ggpk may be compressed with brotli or may be
        a reference to another .dds file.

        This function will take of those kind of files accordingly and try to return
        a file instead.
        If any problems arise an error will be raised instead.

        Parameters
        ----------
        data
            The raw data to extract the dds from.

        Returns
        -------
        bytes
            the uncompressed, dereferenced .dds file data

        Raises
        -------
        ValueError
            If the file data contains a reference, but path_or_ggpk is not specified
        TypeError
            If the file data contains a reference, but path_or_ggpk is of invalid
            type (i.e. not str or :class:`GGPKFile`
        ParserError
            If the uncompressed size does not match the size in the header
        brotli.error
            If whatever bytes were read were not brotli compressed
        """
        # Already a DDS file, so return it
        if data[:4] == b'DDS ':
            return data
        # Is this a reference?
        elif data[:1] == b'*':
            path = data[1:].decode()
            data = self.get_file(path)
            return self.extract_dds(data)
        else:
            size = int.from_bytes(data[:4], 'little')
            dec = brotli.decompress(data[4:])
            if len(dec) != size:
                raise ParserError(
                    'Decompressed size does not match size in the header'
                )
            return dec

    def build_directory(self) -> FileSystemNode:
        """
        Builds a joint directory from the files available on disk, in ggpk and
        in bundles.

        The directory is not required to retrieve files from the file system
        and serves more educational purposes.

        Returns
        -------
            The directory.
        """
        self.directory = FileSystemNode(
            file_system=self,
            name='',
            parent=None,
            file_system_type=FILE_SYSTEM_TYPES.ROOT,
            is_file=False,
        )

        for path, directories, files in os.walk(self.root_path):
            p = os.path.commonprefix([self.root_path, path])
            node = self.directory[path.replace(p, '')]
            params = {
                'file_system': self,
                'parent': node,
                'file_system_type': FILE_SYSTEM_TYPES.DISK,
            }
            for name in directories:
                node.children[name] = FileSystemNode(
                    name=name,
                    is_file=False,
                    **params
                )
            for name in files:
                node.children[name] = FileSystemNode(
                    name=name,
                    is_file=True,
                    **params
                )

        if self.ggpk:
            def add_to_directory(node, depth):
                # Return at depth 0? Root object

                if node.parent:
                    root = self.directory[node.parent.get_path()]
                else:
                    root = self.directory

                root.children[node.name] = FileSystemNode(
                    file_system=self,
                    name=node.name,
                    file_system_type=FILE_SYSTEM_TYPES.GGPK,
                    is_file=node.is_file,
                    parent=root,
                )
            self.ggpk.directory.walk(function=add_to_directory)

        for dir_record in self.index.directories.values():
            parent = self.directory
            for directory in dir_record.path.split('/'):
                try:
                    parent = parent.children[directory]
                except KeyError:
                    node = FileSystemNode(
                        file_system=self,
                        name=directory,
                        file_system_type=FILE_SYSTEM_TYPES.BUNDLE,
                        is_file=False,
                        parent=parent
                    )
                    parent.children[directory] = node
                    parent = node

            for file_name in dir_record.files:
                node = FileSystemNode(
                    file_system=self,
                    name=file_name,
                    file_system_type=FILE_SYSTEM_TYPES.BUNDLE,
                    is_file=True,
                    parent=parent
                )
                parent.children[file_name] = node

        return self.directory

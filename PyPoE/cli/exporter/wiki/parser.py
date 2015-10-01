"""
Path     PyPoE/cli/exporter/wiki/handler.py
Name     Wiki Export Handler
Version  1.0.0a0
Revision $Id$
Author   [#OMEGA]- K2

INFO

Base classes and related functions for Wiki Export Handlers.


AGREEMENT

See PyPoE/LICENSE


TODO

...
"""

# =============================================================================
# Imports
# =============================================================================

# self
from PyPoE.cli.core import console, Msg
from PyPoE.poe.file.dat import RelationalReader
from PyPoE.poe.file.translations import TranslationFileCache

# =============================================================================
# Classes
# =============================================================================


class BaseParser(object):
    _files = []
    _translations = []

    def __init__(self, base_path, data_path, desc_path):
        self.base_path = base_path
        self.data_path = data_path
        self.desc_path = desc_path

        opt = {
            'use_dat_value': False,
        }

        # Load rr and translations which will be undoubtedly be needed for
        # parsing
        self.rr = RelationalReader(data_path, files=self._files, options=opt)
        self.tc = TranslationFileCache(base_path)
        for file_name in self._translations:
            self.tc[file_name]

    def _get_stats(self, mod, translation_file='stat_descriptions.txt'):
        stats = []
        for i in range(1, 6):
            stat = mod['StatsKey%s' % i]
            if stat:
                stats.append(stat)

        ids = []
        values = []
        for i, stat in enumerate(stats):
            j = i + 1
            values.append([mod['Stat%sMin' % j], mod['Stat%sMax' % j]])
            ids.append(stat['Id'])

        tf = self.tc[translation_file]

        effects = tf.get_translation(ids, values)
        if not effects:
            console("%s %s" % (ids, values))

        return tf.get_translation(ids, values)

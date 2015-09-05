"""
Path     PyPoE/tests/test_data
Name     Tests for _data/dat.specification.ini
Version  1.0.0a0
Revision $Id$
Author   [#OMEGA]- K2

INFO

Tests for for the specifications found in dat.specification.ini.
Running this test is relatively time-consuming, so it may be a good idea to
avoid it unless a PoE update has been released to locate broken or unsupported
.dat files.


AGREEMENT

See PyPoE/LICENSE


TODO

...
"""

# =============================================================================
# Imports
# =============================================================================

# Python
import os.path
import warnings

# 3rd Party
import pytest

# self
from PyPoE.poe.constants import DISTRIBUTOR, VERSION
from PyPoE.poe.path import PoEPath
from PyPoE.poe.file import dat, ggpk

# =============================================================================
# Functions
# =============================================================================

def read_ggpk():
    path = PoEPath(
        version=VERSION.STABLE,
        distributor=DISTRIBUTOR.INTERNATIONAL,
    ).get_installation_paths()
    if path:
        path = path[0]
    else:
        warnings.warn('PoE not found, skipping test.')
        return

    contents = ggpk.GGPKFile(os.path.join(path, 'content.ggpk'))
    contents.read()
    root = contents.directory_build()

    file_set = set()

    for node in root['Data'].files:
        name = node.record.name
        if not name.endswith('.dat'):
            continue

        file_set.add(name)

    return root, file_set

# =============================================================================
# Tests
# =============================================================================

root, file_set = read_ggpk()

@pytest.mark.parametrize("node",
    [root['Data'][fn] for fn in file_set],
)
def test_definitions(node):
    opt = {
        'use_dat_value': False,
    }
    # Will raise errors accordingly if it fails
    df = dat.DatFile(node.name, options=opt)
    df.read_from_raw(node.record.extract())




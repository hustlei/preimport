# -*- coding: utf-8 -*-
"""test scripts for preimport module by pytest

:author: lileilei
:email: hustlei@sina.cn
"""

import sys
sys.path.append(".")
from preimport import preimport

MODULE_NAMES = ('numpy', 'PyQt5.QtCore')


def test_preimport(capsys):
    print("")
    preimport(MODULE_NAMES)
    for module in MODULE_NAMES:
        assert module in sys.modules


def test_already_imported(capsys):
    print("")
    import os
    preimport('os')
    out, err = capsys.readouterr()
    print(out)
    assert 'already' in out
    assert 'os' in sys.modules


def test_import_failed(capsys):
    print("")
    preimport("wrong name", "noInstalledMudule")
    out, err = capsys.readouterr()
    print(out)
    assert "failed" in out


def test_import_argerr(capsys):
    print("")
    preimport(1, object())
    out, err = capsys.readouterr()
    print(out)
    assert "check" in out
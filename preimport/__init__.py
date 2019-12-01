# -*- coding: utf-8 -*-
"""function for preimport python module

| author: lileilei
| email: hustlei@sina.cn
"""


def _get_version(default='x.x.x.dev'):
    """get version that automatic generated by setuptools_scm, when setup() running.
    return an obviously wrong version string 'x.x.x.dev' when error.
    """
    try:
        from pkg_resources import DistributionNotFound, get_distribution
    except ImportError:
        return default
    else:
        try:
            return get_distribution(__package__).version
        except DistributionNotFound:  # Run without install
            return default
        except ValueError:  # Python 3 setup
            return default
        except TypeError:  # Python 2 setup
            return default


__version__ = _get_version()
# from setuptools_scm import get_version
# __version__ = get_version(root='..', relative_to=__file__)

from . import core

preimport = core.preimport
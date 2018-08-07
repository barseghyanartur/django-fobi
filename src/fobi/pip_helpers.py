"""
Pip helpers module.
"""
import subprocess
import sys

__title__ = 'fobi.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'check_if_installed',
    'get_installed_packages',
)


def get_installed_packages(with_versions=False):
    """Get installed packages.

    :param with_versions: If set to True, returned with versions.
    :type with_versions: bool
    :return:
    :rtype: list
    """
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    if with_versions:
        return set([r.decode().split('==') for r in reqs.split()])
    else:
        return set([r.decode().split('==')[0] for r in reqs.split()])


def check_if_installed(package, installed_packages=None):
    """Check if package is installed.

    :param package:
    :param installed_packages:
    :type package: str
    :type installed_packages: iterable
    :return:
    :rtype: bool
    """
    if installed_packages is None:
        installed_packages = get_installed_packages(with_versions=False)
    return package in installed_packages

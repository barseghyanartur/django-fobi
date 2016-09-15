__title__ = 'fobi.app'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('app_name', 'app_config',)


def app_name(path, reduce_depth_by=1):
    """Return another path by reducing the depth by one.

    :param str path: Absolute app path (from project root).
    :param int reduce_depth_by:
    :return str:
    """
    return '.'.join(path.split('.')[:-reduce_depth_by])


def app_config(path, config_app_path='apps.Config'):
    """App config.

    :param str path: Absolute app path (from project root).
    :param str config_app_path: Relative config path (from app root)
    :return str:
    """
    return "{0}.{1}".format(path, config_app_path)

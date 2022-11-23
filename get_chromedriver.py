"""
Get chromedriver-py version most suitable for your system.
"""
import argparse
import json
import logging
import os
import re
from pprint import pprint
from shlex import split
from subprocess import check_output
from urllib.request import urlopen

__title__ = "get_chromedriver.py"
__version__ = "0.1"
__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022 Artur Barseghyan"
__license__ = "GPL 2.0/LGPL 2.1"

parser = argparse.ArgumentParser(
    description="Get chromedriver-py version most suitable for your system"
)
parser.add_argument(
    "-v", "--verbose", help="increase output verbosity", action="store_true"
)

args = parser.parse_args()
if args.verbose:
    logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

res = check_output(split("chromium --version"))

pattern = re.compile(r".*chromium\s([0-9]+(\.[0-9]+)+)\s.*", re.IGNORECASE)
version = pattern.match(res.decode()).groups()[0]
logger.info(f"version={version}")

response = urlopen("https://pypi.org/pypi/chromedriver-py/json")

data = json.loads(response.read())
releases = list(data["releases"].keys())
logger.info(f"releases={releases}")

releases_tree = {}
for __version in releases:
    __t = releases_tree  # noqa
    for part in __version.split("."):
        __t = __t.setdefault(part, {"version": __version})

logger.info(f"tree={releases_tree}")

pprint(releases_tree)


def get_closest_version(try_version, tree):
    if not try_version:
        logger.info(f"Exhausted trying to get closest version. Quitting.")
        return None

    logger.info(f"try_version={try_version}")
    _try_version = try_version.split(".")
    if _try_version[0] in tree:
        return get_closest_version(".".join(_try_version[1:]), tree[_try_version[0]])
    else:
        return tree["version"]


closest_version = get_closest_version(version, releases_tree)

if closest_version:
    logger.info(f"closest_version={closest_version}")
    logger.info(f"installing chromedriver-py=={closest_version}")
    os.system(f"pip install chromedriver-py=={closest_version}")

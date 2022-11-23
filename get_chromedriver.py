"""
Get chromedriver-py version most suitable for your system.
"""
import argparse
import json
import logging
import os
import re
from collections import defaultdict
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

try_version = ".".join(version.split(".")[:-1])
logger.info(f"try_version={try_version}")

grouped_releases = defaultdict(list)
logger.info(f"grouped_releases={grouped_releases}")

for __version in releases:
    __key = ".".join(__version.split(".")[:-1])
    grouped_releases[__key].append(__version)

closest_version = grouped_releases.get(try_version)[-1]
logger.info(f"closest_version={closest_version}")

os.system(f"pip install chromedriver-py=={closest_version}")

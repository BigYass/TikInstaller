import argparse
from config import path

from data.text import lang, KEYS

parser:argparse.ArgumentParser = argparse.ArgumentParser(description=lang[KEYS.EXE_DESCRIPTION])

# Server Type
parser.add_argument(
  '--server-type', '-t',
  choices=['paper', 'fabric', 'forge'],
  help = lang[KEYS.ARGS_HELP_SERVER_TYPE],
  default='paper'
)

# Server Version
parser.add_argument(
  '--server-version',
  help = lang[KEYS.ARGS_HELP_SERVER_VERSION],
  default='latest'
)

# Java Version
parser.add_argument(
  '--java_version',
  help = lang[KEYS.ARGS_HELP_JAVA_VERSION],
  default = '22'
)

args:argparse.Namespace = parser.parse_args()
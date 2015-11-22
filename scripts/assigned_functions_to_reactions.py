from PyFBA import filters
from PyFBA import parse

__author__ = 'Rob Edwards'

import argparse
import os
import sys

parser=argparse.ArgumentParser(description='Convert an assigned_functions file to a list of roles')
parser.add_argument('-a', help='assigned functions file', required=True)
parser.add_argument('-v', help='verbose', action='store_true')
args = parser.parse_args()

af = parse.read_assigned_functions(args.a)
rc = filters.roles_to_reactions(af.values())
reactions = set()
for r in rc:
    reactions.update(rc[r])
print("\n".join(reactions))

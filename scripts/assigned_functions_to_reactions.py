from PyFBA import filters
from PyFBA import parse

__author__ = 'Rob Edwards'

import argparse
import os
import sys

parser=argparse.ArgumentParser(description='Convert an assigned_functions file to a list of reactions')
parser.add_argument('-a', help='assigned functions file')
parser.add_argument("-r", help="roles only file (no pegs)")
parser.add_argument('-v', help='verbose', action='store_true')
args = parser.parse_args()

if args.a:
    af = parse.read_assigned_functions(args.a)
    roles = set(af.values())
elif args.r:
    roles =set()
    with open(args.r, 'r') as f:
        for l in f:
            roles.add(l.strip())
else:
    sys.exit('Either -a or -r must be specified')

rc = filters.roles_to_reactions(roles)
reactions = set()
for r in rc:
    reactions.update(rc[r])
print("\n".join(reactions))

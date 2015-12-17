import os
import sys

import argparse
import PyFBA
__author__ = 'Rob Edwards'

parser = argparse.ArgumentParser(description='print reactions associated with roles')
parser.add_argument('-x', help='reaction id(s)', action='append')
parser.add_argument('-f', help='functional role(s)', action='append')
args = parser.parse_args()

if args.x:
    for r in args.x:
        roles = PyFBA.filters.reactions_to_roles(r)
        for rid in roles:
            print("{}\t{}".format(rid, roles[rid]))
if args.f:
    for r in args.f:
        reactions = PyFBA.filters.roles_to_reactions(r)
        for rid in reactions:
            print("{}\t{}".format(rid, reactions[rid]))
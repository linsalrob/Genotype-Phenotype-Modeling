import os
import sys

import argparse
import PyFBA
__author__ = 'Rob Edwards'

parser = argparse.ArgumentParser(description='print reactions associated with roles')
parser.add_argument('-r', help='reaction id(s)', action='append', required=True)
args = parser.parse_args()

for r in args.r:
    roles = PyFBA.filters.reactions_to_roles(r)
    for rid in roles:
        print("{}\t{}".format(rid, roles[rid]))
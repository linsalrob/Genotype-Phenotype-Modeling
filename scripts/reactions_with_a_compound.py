import os
import sys

import PyFBA
import argparse
__author__ = 'Rob Edwards'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='from a list of reactions, find those with a specific compound')
    parser.add_argument('-r', help='file with a list of reactions', required=True)
    parser.add_argument('-c', help='compound name', required=True)
    parser.add_argument('-l', help='compound location (if known/desired)', default='')
    args = parser.parse_args()

    compounds, reactions, enzymes = PyFBA.parse.compounds_reactions_enzymes('gramnegative')

    test_compound = PyFBA.metabolism.Compound(args.c, args.l)

    rcts = set()
    with open(args.r, 'r') as fin:
        for l in fin:
            l = l.strip()
            if l in reactions:
                if test_compound in reactions[l].all_compounds():
                    print("{}\t{}".format(l, reactions[l].equation))



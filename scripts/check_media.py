import argparse
import os
import sys

import PyFBA
__author__ = 'Rob Edwards'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='from a list of reactions, find those with a specific compound')
    parser.add_argument('-r', help='file with a list of reactions', required=True)
    parser.add_argument('-m', help='media file', required=True)
    args = parser.parse_args()

    compounds, reactions, enzymes = PyFBA.parse.compounds_reactions_enzymes('gramnegative')
    media = PyFBA.parse.read_media_file(args.m)
    reactions2run = set()

    with open(args.r, 'r') as fin:
        for l in fin:
            l = l.strip()
            if l in reactions:
                reactions2run.add(l)
            else:
                sys.stderr.write("Skipped {}\n".format(l))

    suggest = set()
    for c in media:
        sys.stderr.write("Compound {}: {}\n".format(c, str(c)))
        rxns = compounds[str(c)].all_reactions()
        importrxn = rxns.intersection(reactions2run)
        sys.stderr.write("    Import: {}\n".format(importrxn))
        if len(importrxn) == 0:
            sys.stderr.write(str(c) + " is not imported\n")
            suggest.update(rxns)
        suggest = {r for r in suggest if r in reactions and r not in reactions2run}

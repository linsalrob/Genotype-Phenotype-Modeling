"""
List the reactions and equations in a model
"""

import os
import sys
import argparse
import PyFBA

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="List the reactions and equations in a model")
    parser.add_argument('-r', help='Reactions file', required=True)
    args = parser.parse_args()

    # read the enzyme data
    compounds, reactions, enzymes = PyFBA.parse.model_seed.compounds_reactions_enzymes('gramnegative')

    reactions2run = set()
    with open(args.r, 'r') as f:
        for l in f:
            if l.startswith('#'):
                continue
            if "biomass" in l:
                if args.v:
                    sys.stderr.write("Biomass reaction was skipped from the list as it is auto-imported\n")
                continue
            r = l.strip()
            if r in reactions:
                reactions2run.add(r)

    for r in reactions2run:
        print(r + " : " + reactions[r].equation)

import copy
import os
import sys

import PyFBA
import argparse
__author__ = 'Rob Edwards'

# list the import export reactions for  a model
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check import and output reactions')
    parser.add_argument('-r', help='reactions file', required=True)
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
            else:
                sys.stderr.write("Reaction {} skipped\n".format(r))

    ioreactions = set()
    for r in reactions2run:
        if reactions[r].is_transport or reactions[r].is_uptake_secretion:
            ioreactions.add(r)

    # read the negative control
    media = PyFBA.parse.read_media_file('tempmedia/MOPS_NoC_Negative_Control.txt')
    biomass_eqtn = PyFBA.metabolism.biomass_equation('gramnegative')
    status, value, growth = PyFBA.fba.run_fba(compounds, reactions, reactions2run, media, biomass_eqtn)
    print("BEFORE REMOVING: {} {} and {}".format(len(reactions2run), value, growth))

    flux = PyFBA.fba.reaction_fluxes()

    for r in ioreactions:
        print("{}\t{}\t{}\t{}\t{}".format(r, flux[r], reactions[r].is_uptake_secretion, reactions[r].is_transport, reactions[r].equation))



    sys.exit()
    ori = copy.copy(reactions2run)
    for r in ioreactions:
        reactions2run = copy.copy(ori)
        reactions2run.remove(r)
        status, value, growth = PyFBA.fba.run_fba(compounds, reactions, reactions2run, media, biomass_eqtn)
        print("{}\t{}".format(r, growth))
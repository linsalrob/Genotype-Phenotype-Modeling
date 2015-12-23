import os
import sys

import PyFBA
import argparse
__author__ = 'Rob Edwards'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Measure growth of a model on all media in a directory')
    parser.add_argument('-r', help='reactions file', required=True)
    parser.add_argument('-m', help='media directory', required=True)
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

    print("We have {} reactions to run".format(len(reactions2run)))

    biomass_eqtn = PyFBA.metabolism.biomass.biomass_equation('gramnegative')

    for mediaf in os.listdir(args.m):
        if not mediaf.endswith('.txt'):
            sys.stderr.write("Skipped media file: {} as the file ending is not .txt\n".format(mediaf))
            continue
        media = PyFBA.parse.read_media_file(os.path.join(args.m, mediaf))
        print("Media file is {}".format(os.path.join(args.m, mediaf)))
        status, value, growth = PyFBA.fba.run_fba(compounds, reactions, reactions2run, media, biomass_eqtn)
        print("{}\t{}\t{}".format(mediaf, value, growth))
        # reset uptake secretion reactions
        for r in reactions2run:
            reactions[r].is_uptake_secretion = False

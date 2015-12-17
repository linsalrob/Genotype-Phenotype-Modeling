import copy
import os
import sys

import PyFBA
import argparse
__author__ = 'Rob Edwards'

parser = argparse.ArgumentParser(description='Delete one or more reactions from a model and then see if we can gapfill with reactions with proteins. If so, bissect them out')
parser.add_argument('-r', help='list of reactions in model', required=True)
parser.add_argument('-d', help='reaction(s) to delete', required=True, action='append')
parser.add_argument('-m', help='media file', required=True)
args = parser.parse_args()

reactions_to_run = set()
compounds, reactions, enzymes = PyFBA.parse.compounds_reactions_enzymes('gramnegative')
media = PyFBA.parse.read_media_file(args.m)
biomass_eqtn = PyFBA.metabolism.biomass.biomass_equation('gramnegative')

with open(args.r, 'r') as fin:
    for l in fin:
        if l.strip() in reactions:
            reactions_to_run.add(l.strip())
        else:
            sys.stderr.write("Skipped reaction {}\n".format(l.strip()))

sys.stderr.write("Before removing reactions, we have {} reactions to run\n".format(len(reactions_to_run)))
for r in args.d:
    reactions_to_run.remove(r)
sys.stderr.write("After removing reactions, we have {} reactions to run\n".format(len(reactions_to_run)))

status, value, growth = PyFBA.fba.run_fba(compounds, reactions, reactions_to_run, media, biomass_eqtn)
sys.stderr.write("Initial model with deleted reactions FBA: {} (growth is {})\n\n".format(value, growth))

if growth:
    sys.exit("No need to gapfill!")

original_reactions = copy.copy(reactions_to_run)

# propose other reactions that we have proteins for
with_p_reactions = PyFBA.gapfill.suggest_reactions_with_proteins(reactions, verbose=True)
# find the new reactions
with_p_reactions.difference_update(reactions_to_run)
reactions_to_run.update(with_p_reactions)

status, value, growth = PyFBA.fba.run_fba(compounds, reactions, reactions_to_run, media, biomass_eqtn)
sys.stderr.write("After adding {} reactions with proteins ".format(len(with_p_reactions)) +
                 " we get {} (growth is {})\n\n".format(value, growth))

if growth:
    new_essential = PyFBA.gapfill.minimize_additional_reactions(original_reactions, with_p_reactions,compounds, reactions, media, biomass_eqtn, True)
    sys.stderr.write("In the end we needed to add {} reactions to grow\n".format(len(new_essential)))
    for r in original_reactions:
        print("{}\t{}".format(r, args.r))
    for r in new_essential:
        print("{}\t{}".format(r, "GAPFILLED"))
else:
    sys.stderr.write("We could not gapfill for the deletion of {} and get growth\n".format(args.d))

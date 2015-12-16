import copy

import PyFBA
import os
import sys

import argparse

parser = argparse.ArgumentParser(description='Test growth of a model, allowing for knockouts')
parser.add_argument('-r', help='reaction list to create model from', required=True)
parser.add_argument('-m', help='media file', required=True)
parser.add_argument('-k', help='optional reactions to knock out', action='append', default=[])
args = parser.parse_args()

media = PyFBA.parse.read_media_file(args.m)
compounds, reactions, enzymes = PyFBA.parse.compounds_reactions_enzymes('gramnegative')
biomass_equation = PyFBA.metabolism.biomass_equation('gramnegative')

# read the reaction list
reactions_to_run = set()
with open(args.r, 'r') as fin:
    for l in fin:
        if l.strip() in reactions:
            reactions_to_run.add(l.strip())
        else:
            sys.stderr.write("Skipped reaction {}\n".format(l.strip()))

status, value, growth = PyFBA.fba.run_fba(compounds, reactions, reactions_to_run, media, biomass_equation)
print("Initial run has {} --> Growth: {}".format(value, growth))

# now delete all reactions
ori_r2r = copy.copy(reactions_to_run)
for r in args.k:
    reactions_to_run = copy.copy(ori_r2r)
    assert isinstance(reactions_to_run, set)
    reactions_to_run.remove(r)
    status, value, growth = PyFBA.fba.run_fba(compounds, reactions, reactions_to_run, media, biomass_equation)
    print("After removing {} run has {} --> Growth: {}".format(r, value, growth))
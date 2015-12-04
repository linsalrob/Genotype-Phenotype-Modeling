import os
import sys

__author__ = 'Rob Edwards'

"""
Count the total number of compounds and reactions in a model
"""

import PyFBA.parse.SBML

import argparse
parser = argparse.ArgumentParser(description='Count the combination of reactions and compounds in a model')
parser.add_argument('-s', help='SBML file', required=True)
args = parser.parse_args()

sbml = PyFBA.parse.SBML.parse_sbml_file(args.s)

n = 0
intra = set()
extra = set()
reactions = sbml.get_all_reactions()
for r in reactions:
    for compound in  reactions[r].all_compounds():
        if compound.location == 'e':
            extra.add(str(compound))
        else:
            intra.add(str(compound))
        n+=1

print("Number of reaction/compounds: {}".format(n))

print("The Citrobacter model includes {} intracellular reactions and {} extracellular compounds".format(len(intra), len(extra)))
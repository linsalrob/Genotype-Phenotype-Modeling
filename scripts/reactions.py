import os
import sys
import re
__author__ = 'Rob Edwards'

"""
Generate some information about reactions for the paper
"""

import PyFBA

compounds, reactions, enzymes = PyFBA.parse.compounds_reactions_enzymes('gram_negative')
roles = PyFBA.parse.model_seed.roles()
# some general information
cloc = {}
allc = set()
for c in compounds:
    allc.add(compounds[c].name)
    cloc[compounds[c].location] = cloc.get(compounds[c].location, 0) + 1

print("There are {} compounds".format(len(allc)))
for l in cloc:
    print("{} compounds are in {}".format(cloc[l], l))

allr = set()
rwithp = set()
for r in reactions:
    allr.add(reactions[r].name)
    if reactions[r].number_of_enzymes() > 0:
        rwithp.add(reactions[r].name)

print("There are {} reactions".format(len(allr)))
print("There are {} reactions associated with proteins".format(len(rwithp)))


# find some roles that are in multiple complexes
if False:
    for r in sorted(roles):
        if len(roles[r]) > 1:
            print("{}\t{}\t{}".format(r, len(roles[r]), roles[r]))


if False:
    # Looking at the specific enzymes associated with functional roles
    # Phosphoenolpyruvate-protein phosphotransferase of PTS system (EC 2.7.3.9)
    # Glutamate synthase [NADH] (EC 1.4.1.14)
    for c in roles['Phosphoenolpyruvate-protein phosphotransferase of PTS system (EC 2.7.3.9)']:
        if c in enzymes:
            for r in enzymes[c].reactions:
                print("{}\t{}\t{}".format(c, r, reactions[r].equation))
            for r in enzymes[c].roles:
                print("{}\t{}".format(c, r))
        else:
            sys.stderr.write("{} not found in enzymes\n".format(c))
        print("\n")


if False:
    # looking for two different EC numbers asssociated with the same complex
    for c in enzymes:
        ec = set()
        ro = set()
        for r in enzymes[c].roles:
            m = re.search('EC \d+\.\d+\.\d+\.\d+', r)
            if m and m.group() not in ec:
                ec.add(m.group())
                ro.add(r)
        if len(ec) > 1:
            print(c + "\t" + "\t".join(ro) + "\n")

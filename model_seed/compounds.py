from PyFBA import parse

__author__ = 'Rob Edwards'

cmpds, reactions, enzs = parse.compounds_reactions_enzymes()

for c in cmpds:
    # :type cmpds[c]: PyFBA.metabolism.compound.Compound
    print("{}\t{}\t{}".format(cmpds[c].name, cmpds[c].location, cmpds[c].model_seed_id))

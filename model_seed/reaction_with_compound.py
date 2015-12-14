import os
import sys

from PyFBA import parse
from PyFBA.metabolism import Compound

__author__ = 'Rob Edwards'


def find_compound(name, location):
    """
    FInd all reactions with a compound

    :param name: The name of the compound
    :type name: str
    :param location: The location of the compound
    :type location: str
    :return:
    :rtype:
    """
    cpds, rcts, enz = parse.compounds_reactions_enzymes()

    test = Compound(name, location)
    for rid in rcts:
        # :type rcts[r]: PyFBA.metabolism.Reaction
        if test in rcts[rid].all_compounds():
            print("{}\t{}".format(rid, rcts[rid].equation))

if __name__ == '__main__':
    try:
        nm = sys.argv[1]
        loc = sys.argv[2]
    except:
        sys.exit(sys.argv[0] + " <name of compound> <location of compound>")

    find_compound(nm, loc)
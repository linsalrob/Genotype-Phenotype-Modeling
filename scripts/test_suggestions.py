import os
import sys

import PyFBA

__author__ = 'Rob Edwards'

try:
    testF = sys.argv[1]
except:
    sys.exit(sys.argv[0] + " <test file>")


compounds, reactions, enzymes = PyFBA.parse.compounds_reactions_enzymes('gramnegative')

close_reactions = PyFBA.gapfill.suggest_from_roles(testF, reactions, threshold=0, verbose=True)

print("Proposed reactions\n" + "\n".join(close_reactions))

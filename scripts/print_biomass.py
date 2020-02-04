import sys
import PyFBA

b = PyFBA.metabolism.biomass.biomass_equation('gramnegative')

for m in b.left_compounds:
    sys.stdout.write(" + ({0:.2f}) {1}".format(b.get_left_compound_abundance(m), m.name))
sys.stdout.write(" => ")
for m in b.right_compounds:
    sys.stdout.write(" + ({0:.2f}) {1}".format(b.get_right_compound_abundance(m), m.name))
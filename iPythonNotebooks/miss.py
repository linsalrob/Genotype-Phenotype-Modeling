
import PyFBA


sone = set()
with open('C.sedlakii_gf_MOPS.reactions', 'r') as fin:
    for l in fin:
        sone.add(l.strip())

stwo = set()
with open('our_reactions.txt', 'r') as fin:
    for l in fin:
        stwo.add(l.strip())

missed = set()
for s in sone:
    if s not in stwo:
        missed.add(s)


roles = PyFBA.filters.reactions_to_roles(missed)
rolesneeded = set()
for m in missed:
    if m not in roles:
        roles[m] = set()
    rolesneeded.update(roles[m])
    print("{}\t{}".format(m, roles[m]))


roles_to_add = set()
with open('/data/FuzzyMetabolicNetworks/models/Citrobacter/263199/citrobacter.roles', 'r') as fin:
    for l in fin:
        p=l.strip().split("\t")
        roles_to_add.add(p[0])

print("\n\n")

for r in missed:
    willadd = False
    for role in roles[r]:
        if role in roles_to_add:
            willadd = True
    if not willadd:
        print("Will not add: {}\t{}".format(r, roles[r]))

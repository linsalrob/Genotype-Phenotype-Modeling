import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Parse the reaction output lists and figure out the union of them')
parser.add_argument('-r', help='reaction output file', action='append')
args = parser.parse_args()

data = []
filename = []
for rf in args.r:
    filename.append(rf)
    with open(rf, 'r') as f:
        c=["{"]
        for l in f:
            c.append(l.strip())
        c.append("}")
        code = eval("".join(c))
        data.append(code['reactions'])

# print("Data has length ".format(len(data)))

dist = []
for i in range(len(data)):
    dist.append([0 for r in range(len(data))])

#print("DATA: ".format(dist))

for i in range(len(data)):
    dist[i][i] = len(data[i])
    for j in range(len(data)):
        if j < i:
            dist[i][j] = len(data[i].intersection(data[j]))
            dist[j][i] = len(data[i].union(data[j]))
        elif j > i:
            dist[j][i] = len(data[i].intersection(data[j]))
            dist[i][j] = len(data[i].union(data[j]))

print("\t" + "\t".join(filename))
for i in (range(len(data))):
    print(filename[i] + "\t" + "\t".join(map(str, dist[i])))


'''
Compare growth of media to actual growth
'''
import sys

__author__ = 'Rob Edwards'


import argparse


parser = argparse.ArgumentParser(description='Compare growth of media predicted by FBA to actual growth')
parser.add_argument('-a', help='actual grow file', required=True)
parser.add_argument('-b', help='column in actual growth file (default = last column)', type=int)
parser.add_argument('-p', help='predicted growth file', required=True)
parser.add_argument('-q', help='column in predicted growth file (default = last column)', type=int)
parser.add_argument('-l', help='list comparisons between truth and predictions', action='store_true')
parser.add_argument('-v', help='verbose output', action='store_true')
args = parser.parse_args()

truth_col = args.b or -1
pred_col = args.q or -1

truth = {}
with open(args.a, 'r') as f:
    for l in f:
        if l.startswith('#') or l.lower().startswith('media'):
            continue
        p=l.strip().split('\t')
        truth[p[0].replace('.txt', '')] = p[truth_col]

pred = {}
with open(args.p, 'r') as f:
    for l in f:
        if l.startswith('#') or l.lower().startswith('media'):
            continue
        p = l.strip().split('\t')
        pred[p[0].replace('.txt', '')] = p[pred_col]

diff = 0
same = 0
print("Media\tTruth\tPredictions\tResult")
for t in truth:
    if t not in pred:
        if args.v:
            sys.stderr.write("Warning: " + t + " not in predictions\n")
        diff += 1
        pred[t] = "NULL"
        samediff = "DIFFERENT"
    elif pred[t] == truth[t]:
        same += 1
        samediff = "SAME"
    else:
        diff += 1
        samediff = "DIFFERENT"

    if args.l:
        print(t + "\t" + truth[t] + "\t" + pred[t] + "\t" + samediff)

for p in pred:
    if p in truth:
        continue
    if args.v:
        sys.stderr.write("Warning: " + p + " not in truth\n")
    diff += 1
    if args.l:
        print(p + "\tNULL\t" + pred[p] + "\tDIFFERENT\n")

print("Same assertions: " + str(same) +  " Different assertions: " + str(diff))

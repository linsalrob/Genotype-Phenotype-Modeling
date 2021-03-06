import os
import sys

import argparse
__author__ = 'Rob Edwards'

if __name__ == '__main__':
    print_types = ['tp', 'fp', 'tn', 'fn']
    parser = argparse.ArgumentParser(description='Compare predictions to reality')
    parser.add_argument('-r', help='reality file that has id, media, and growth level etc (probably ../growth_predictions.tsv', required=True)
    parser.add_argument('-p', help='predictions file', required=True)
    parser.add_argument('-g', help='genome id. Use the RAST id (2nd column in reality file')
    parser.add_argument('-o', help='print one class of results. Options: {}'.format(print_types), default=None)
    args = parser.parse_args()

    growth = {}
    with open(args.r, 'r') as f:
        for l in f:
            p=l.strip().split('\t')
            if len(p) < 4:
                sys.stderr.write("Can't parse growth from {}".format(l))
                continue
            if p[1] not in growth:
                growth[p[1]] = {}
            growth[p[1]][p[3]]=p[4]

    if args.g not in growth:
        sys.exit("{} was not found in {}. Can not continue\n".format(args.g, args.r))

    predict = {}
    value = {}
    with open(args.p, 'r') as f:
        for l in f:
            p=l.strip().split('\t')
            if len(p) < 2:
                sys.stderr.write("can't parse growth from predictions {}".format(l))
                continue
            if p[2] == "True":
                predict[p[0]] = True
            else:
                predict[p[0]] = False
            value[p[0]] = p[1]

    tp = 0
    fp = 0
    fn = 0
    tn = 0

    for p in predict:
        if p not in growth[args.g]:
            sys.stderr.write("Can't find reality for {}. Skipped\n".format(p))
            continue
        if predict[p]:
            if '+' in growth[args.g][p]:
                tp += 1
                if args.o == 'tp':
                    print("tp: {}\t{}\t{}".format(p, growth[args.g][p], value[p]))
            else:
                fp += 1
                if args.o == 'fp':
                    print("fp: {}\t{}\t{}".format(p, growth[args.g][p], value[p]))
        else:
            if '-' in growth[args.g][p]:
                tn += 1
                if args.o == 'tn':
                    print("tn: {}\t{}\t{}".format(p, growth[args.g][p], value[p]))
            else:
                fn += 1
                if args.o == 'fn':
                    print("fn: {}\t{}\t{}".format(p, growth[args.g][p], value[p]))

    print("TP: {}\tTN: {}\tFP: {}\tFN: {}".format(tp, tn, fp, fn))
    if tp + fn > 0:
        print("Sensitivity: {} Precision: {} Accuracy: {}".format(1.0 * tp/(tp + fn), 1.0*tp/(tp + fp), 1.0 * (tp+tn)/(tp + fp + tn + fn)))

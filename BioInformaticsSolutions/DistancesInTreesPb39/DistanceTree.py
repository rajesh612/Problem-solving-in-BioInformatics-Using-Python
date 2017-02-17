import sys
from StringIO import StringIO
from Bio import Phylo
import re


def get_dist(tree, taxa):
    taxa = taxa.split()
    tokens = iter(re.split('([(),])', tree))
    while next(tokens) not in taxa:
        pass
    climbs = 0
    descents = 0
    for token in tokens:
        if token in taxa:
            break
        if token in ',)':
            if descents > 0:
                descents -= 1
            else:
                climbs += 1
        if token in ',(':
            descents += 1
    print climbs + descents ,

if __name__ == '__main__':
    in_file = open('C:/Users/Rajesh/PycharmProjects/DistancesInTreesPb39/rosalind_nwck.txt', 'r')
    pairs = [l.split('\n') for l in in_file.read().strip().split('\n\n')]
    for s, l1 in pairs:
        get_dist(s, l1)

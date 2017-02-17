import re
from itertools import product

def is_kmer(genome, kmer, t):
    if genome.count(kmer) < t:
        return False

    return True

def get_kmer(genome, kmer, l, t):
    positions = [m.start() for m in re.finditer(kmer, genome)]

    if (positions[t - 1] - positions[0] < l):
        return True

    return False


def get_kmer_clumps(genome, k, l, t):
    raw_kmers = [''.join(x) for x in product('ACGT', repeat=k)]
    valid_kmers = set(kmer for kmer in raw_kmers if is_kmer(genome, kmer, t) == True)

    return set(kmer for kmer in valid_kmers if get_kmer(genome, kmer, l, t) == True)


if __name__ == '__main__':
    genome_file = open('C:/Users/Rajesh/PycharmProjects/PatternClumpsPb4/clump.txt').read().strip().split('\n')
    genome = genome_file[0]
    k, l, t = [int(i.strip()) for i in genome_file[1].split(' ')]

    print ' '.join(map(str, get_kmer_clumps(genome, k, l, t)))


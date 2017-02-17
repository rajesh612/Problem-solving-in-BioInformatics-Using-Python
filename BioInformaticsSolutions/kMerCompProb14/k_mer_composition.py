from itertools import product

N_MER = 4
def get_kmer_comp(s, n):
    kmer_dict = {}
    # iterate through list of all substrings in ACGT
    for sub in [''.join(x) for x in product('ACGT', repeat=n)]:
        kmer_dict[sub] = 0

    for i in range(len(s) - (n - 1)):
        sub_str = s[i: i + n]
        kmer_dict[sub_str] += 1
    return kmer_dict

def kmer_comp(dna_str):
    kmer_out = []

    # dna_str[0][1] gives dna string
    kmer_composition = get_kmer_comp(dna_str[0][1], N_MER)

    for kmer in sorted(kmer_composition.iterkeys()):
        kmer_out.append(kmer_composition[kmer])

    return kmer_out

if __name__ == "__main__":
    dna_data =[]
    dna_file = open('C:\Users\Rajesh\PycharmProjects\kMerCompProb14\dna_kmer.txt').read().strip()
    dna_strings = dna_file.strip().split('>')
    for string in dna_strings:
        if len(string):
            item = string.split()
            key = item[0]
            val = ''.join(item[1:])
            dna_data.append((key, val))
    print ' '.join(map(str, kmer_comp(dna_data)))



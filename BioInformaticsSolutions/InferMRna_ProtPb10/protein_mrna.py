stop = 'Stop'
rna_codon = {
    'UUU': 'F',         'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',         'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',         'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',         'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',         'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',         'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',         'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',         'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',         'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',         'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': stop,        'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': stop,        'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',         'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',         'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': stop,        'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',         'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

def rna_string_count(s):
    rna_dict = rna_codeon_count()
    stop_count = rna_dict[stop]

    for s_str in s:
        stop_count *= rna_dict[s_str]

    return stop_count

def rna_codeon_count():
    dict = {}
    for i,j in rna_codon.iteritems():
        if not dict.has_key(j):
            dict[j] = 0

        dict[j] += 1
    return dict

if __name__ == "__main__":
    rna_string = ""
    rna_file = open('C:/Users/Rajesh/PycharmProjects/InferMRna_ProtPb10/rna_string.txt','r')
    for rna in rna_file:
        rna_string += rna.strip()

    print rna_string_count(rna_string) % 1000000



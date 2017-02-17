stop = 'Stop'

# codeon table with T instead of U
codon_dict = {
    'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
    'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
    'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
    'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
    'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
    'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
    'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'TAA': stop, 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'TAG': stop, 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
    'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'TGA': stop, 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


def rev_comp_frame(dna_data):
    map_frame = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([map_frame[d] for d in reversed(dna_data)])


def orf(s):
    s_orf = []
    indices = []
    l = len(s)

    for i in range(l):
        # Splitting s into 3 parts
        protein = codon_trans(s[i: i + 3])

        if protein and protein == 'M':
            indices.append(i)

    for i in indices:
        stop_codeon = False
        protein_str = ''

        for j in range(i, l, 3):
            protein = codon_trans(s[j:j + 3])

            if not protein:
                break

            if protein == stop:
                stop_codeon = True
                break

            protein_str += protein

        if stop_codeon:
            s_orf.append(protein_str)

    return s_orf

def get_dna(dna_fl):
    dna_str = ""

    for l in dna_fl:
        l = l.rstrip()

        if l.startswith(">") == False:
            dna_str = l
    yield dna_str

def codon_trans(codon):
    protein = None

    if len(codon) == 3 and codon_dict.has_key(codon):
        protein = codon_dict[codon]

    return protein


if __name__ == "__main__":
    dna_file = open('C:/Users/Rajesh/PycharmProjects/ORFPb12/rosalind_orf.txt','r')
    for line in get_dna(dna_file):
        start_end = orf(line)
        end_start = orf(rev_comp_frame(line))

        print "\n".join(set(start_end + end_start))
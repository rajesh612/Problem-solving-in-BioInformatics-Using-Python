from Bio.Seq import translate

ncbi_ids = [1,2,3,4,5,6,9,10,11,12,13,14,15]

def translate_dna_prot(dna,prot):
    for i in ncbi_ids:
        if translate(dna, stop_symbol="",table=i) == prot:
            return i

if __name__ == '__main__':
    dna_str,protein_str = open('C:/Users/Rajesh/PycharmProjects/ProtTranslatePb7/dna_prot.txt').read().strip().split('\n')
    print translate_dna_prot(dna_str,protein_str)
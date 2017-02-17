from Bio.Seq import Seq
if __name__== "__main__":
    dna_file = open('C:/Users/Rajesh/PycharmProjects/BioArmoryPb2/dna_seq.txt').read().strip().split()
    for line in dna_file:
        dna_seq = Seq(str(line))
    print dna_seq
    a_count = dna_seq.count('A')
    c_count = dna_seq.count('C')
    g_count = dna_seq.count('G')
    t_count = dna_seq.count('T')
    print a_count,' ',c_count,' ',g_count,' ',t_count

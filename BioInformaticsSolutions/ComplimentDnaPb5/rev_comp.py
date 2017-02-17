from Bio.Seq import Seq
dna_string = open('C:/Users/Rajesh/PycharmProjects/ComplimentDnaPb5/rev_comp.txt','r').readline()
dna_seq = Seq(str(dna_string))
rev_comp = dna_seq.reverse_complement()
print rev_comp


from Bio import Entrez,SeqIO
gen_ids = []
genbank_file =open('C:/Users/Rajesh/PycharmProjects/DataFormatsPb27/rosalind_gen.txt','r')
for line in genbank_file:
    gen_ids.append(line)
print gen_ids
Entrez.email ="rajesh.bommakuri@gmail.com"
data = Entrez.efetch(db="nucleotide",id=gen_ids,rettype="fasta")
strings = SeqIO.parse(data,"fasta")
print min(strings,key =lambda y:len(y.seq)).format('fasta')
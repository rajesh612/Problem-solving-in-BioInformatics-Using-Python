from StringIO import StringIO
from Bio import SeqIO

if __name__== "__main__":
    fastq_file = open('C:/Users/Rajesh/PycharmProjects/FastqIntroPb28/fastq.txt','r')
    fasta_data = StringIO("")

    SeqIO.convert(fastq_file,'fastq',fasta_data,'fasta')

    print fasta_data.getvalue()
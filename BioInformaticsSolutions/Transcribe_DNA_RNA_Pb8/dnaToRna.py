if __name__ == "__main__":
    dna_file = open('C:/Users/Rajesh/PycharmProjects/Transcribe_DNA_RNA_Pb8/dna_file.txt','r')
    for dna_line in dna_file:
        dna_rna_data = dna_line
        rna_data = dna_rna_data.replace('T','U')
        print rna_data


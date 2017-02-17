from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def get_protein(rna):
    rna = Seq(rna, IUPAC.unambiguous_rna)
    return str(rna.translate(to_stop=True))

if __name__ == "__main__":
    rna_file = open('C:/Users/Rajesh/PycharmProjects/RNAToProteinPb9/rna.txt','r')
    rna_data = rna_file.read().strip()
    print get_protein(rna_data)
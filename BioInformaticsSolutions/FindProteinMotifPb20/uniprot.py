import requests
import re
from StringIO import StringIO
from Bio import SeqIO


if __name__ == '__main__':
    file_id = open('C:/Users/Rajesh/PycharmProjects/FindProteinMotifPb20/rosalind_mprt.txt')
    protein_ids = file_id.read().strip().split('\n')
    # read each protein id and get details from uniprot url
    for uniprot in protein_ids:
        protein_details = requests.get('http://www.uniprot.org/uniprot/%s.fasta' % uniprot)

        prot_seq = SeqIO.read(StringIO(protein_details.text), 'fasta')
        location_list = [l for l in re.finditer(r'(?=(N[^P][ST][^P]))', str(prot_seq.seq))]

        if not len(location_list):
            continue

        print(uniprot)

        # Joining list locations
        print(' '.join([str(m.start(0) + 1) for m in location_list]))
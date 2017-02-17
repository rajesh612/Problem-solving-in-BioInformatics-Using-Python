from Bio import ExPASy, SwissProt

if __name__ == '__main__':
    uniprot_file = ExPASy.get_sprot_raw(open('C:/Users/Rajesh/PycharmProjects/ProtDbPb26/rosalind_dbpr.txt').read().strip())
    id = SwissProt.read(uniprot_file)

    bio_proc = [record[2].split(':')[1] for record in id.cross_references
                 if record[0] == 'GO' and record[2].startswith('P')]

    print('\n'.join(bio_proc))
from Bio import SeqIO

def get_lcsm(dna_strings):
    dna = sorted(dna_strings)
    common_str = dna[0]
    dna_str = dna[1:]

    l = len(common_str)
    m = ''
    for i in range(0, l):
        for j in range(l, i + len(m), -1):
            common_sub = common_str[i:j]

            long_com_sub = True
            for n in dna_str:
                if common_sub not in n:
                    long_com_sub = False
                    break

            if long_com_sub:
                m = common_sub
                break
    return m

if __name__ == "__main__":
    dna_strings = []
    for record in SeqIO.parse("C:/Users/Rajesh/PycharmProjects/SharedMotifPb21/rosalind_lcs.txt", "fasta"):
        dna_strings.append(str(record.seq))
print get_lcsm(dna_strings)


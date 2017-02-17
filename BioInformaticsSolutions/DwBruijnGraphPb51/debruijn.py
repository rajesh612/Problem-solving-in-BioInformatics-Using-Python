def rev_comp(s):
    rev_str = ""
    for c in s[::-1]:
        rev_str += "ATGC"["TACG".find(c)]
    return rev_str


if __name__ == '__main__':
    dna_file = open('C:/Users/Rajesh/PycharmProjects/DwBruijnGraphPb51/rosalind_dbru.txt').readlines()
    dna_strings = [i.strip() for i in dna_file]
    out_file = open('C:/Users/Rajesh/PycharmProjects/DwBruijnGraphPb51/dbru_output.txt', 'w')
    dna_list = []
    dict = {}

    for dna in dna_strings:
        dna_list.append(dna)
        dna_list.append(rev_comp(dna))

    for i in range(len(dna_list)):
        dict[dna_list[i][:len(dna_list[i]) - 1], dna_list[i][1:]] = 1

    for d in dict:
        out_file.write(str(d).replace("'", ''))
        out_file.write('\n')

    out_file.close()
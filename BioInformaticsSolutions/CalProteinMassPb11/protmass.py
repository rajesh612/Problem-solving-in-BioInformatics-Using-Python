monoisotopic_mass_dict = {
'A' :  71.03711,
'C' :  103.00919,
'D' :  115.02694,
'E' :   129.04259,
'F' :   147.06841,
'G' :   57.02146,
'H' :   137.05891,
'I' :   113.08406,
'K' :   128.09496,
'L' :   113.08406,
'M' :   131.04049,
'N' : 114.04293,
'P' :   97.05276,
'Q' :   128.05858,
'R' :   156.10111,
'S' :   87.03203,
'T' :   101.04768,
'V' :   99.06841,
'W' :   186.07931,
'Y' :   163.06333
}
if __name__ == '__main__':
    total_weight = 0.0
    protein_str = []
    protein_file = open('C:/Users/Rajesh/PycharmProjects/CalProteinMassPb11/protstring.txt').readline()
    for line in protein_file.strip():
        for l in line:
            if monoisotopic_mass_dict.has_key(l):
                total_weight += monoisotopic_mass_dict[l]

    print round(total_weight,3)

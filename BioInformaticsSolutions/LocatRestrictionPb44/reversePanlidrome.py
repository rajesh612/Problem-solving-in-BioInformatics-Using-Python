def rev_comp(s):
    rev_string = s[::-1]
    compliments = {'A':'T','C':'G','G':'C','T':'A'}
    comp_string = ''.join(compliments[c] for c in rev_string)
    return comp_string

def get_rev_palind(dna):
    for m in range(4,13):
        for n in range(len(dna)-m+1):
            if dna[n:n+m] == rev_comp(dna[n:n+m]):
                yield n,dna[n: n + m]

def get_pos_len(rev_palind):
    for k,dna in sorted(rev_palind):
        print k+1,len(dna)

if __name__ == '__main__':
    dna_string = ""
    dna_file = open('C:/Users/Rajesh/PycharmProjects/LocatRestrictionPb44/rosalind_revp.txt', 'r')

    for line in dna_file:
        line = line.rstrip()
        if line.startswith('>'):
            continue
        else:
            dna_string += line
    get_pos_len(get_rev_palind(dna_string))


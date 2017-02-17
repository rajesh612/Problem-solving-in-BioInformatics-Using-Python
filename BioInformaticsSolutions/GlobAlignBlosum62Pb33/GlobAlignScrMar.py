from itertools import product
from Bio.SubsMat.MatrixInfo import blosum62

def maxAlignscorgMat(s,t):
    string_s = len(s)
    string_t = len(t)
    AlnScore = {(0,0):(0,None)}

    AlnScore.update({((m, 0), (m * -5, (m - 1, 0))) for m in range(1, string_s + 1)})
    AlnScore.update({((0, m), (m * -5, (0, m - 1))) for m in range(1, string_t + 1)})

    for m,n in product(range(1,string_s+1),range(1,string_t+1)):
        cost = blosum62.get((s[m-1],t[n-1]))
        if cost == None:
            cost = blosum62.get((t[n-1],s[m-1]))
        a = AlnScore[(m-1,n-1)][0] + cost
        b = AlnScore[(m - 1, n)][0] - 5
        c = AlnScore[(m, n - 1)][0] - 5
        max_align = max(a,b,c)

        if a == max_align:
            AlnScore[(m, n)] = (max_align,(m-1, n-1))
        elif b == max_align:
            AlnScore[(m, n)] = (max_align,(m-1, n))
        elif c == max_align:
            AlnScore[(m, n)] = (max_align,(m, n-1))
    return AlnScore[(m, n)][0]


if __name__ == '__main__':
    fasta_count = 0
    s_string = []
    t_string = []
    proteinFile = open('C:/Users/Rajesh/PycharmProjects/GlobAlignBlosum62Pb33/rosalind_glob.txt', 'r')
    for line in proteinFile:
        if line.startswith('>'):
            fasta_count += 1
            continue
        elif fasta_count == 1:
            for l in line.strip('\n'):
                s_string.append(l)
        else:
            for m in line.strip('\n'):
                t_string.append(m)

    print s_string
    print t_string
    print maxAlignscorgMat(s_string,t_string)


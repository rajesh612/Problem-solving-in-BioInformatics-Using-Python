from itertools import product
from Bio.SubsMat.MatrixInfo import blosum62

def globAlign(s,t):
    protein_s = len(s)
    protein_t = len(t)
    maximumAlnScore = {(0,0):(0,None)}

    a,b,c ={},{},{}

    maximumAlnScore.update({((m, 0), (-5, (m - 1, 0))) for m in range(1, protein_s + 1)})
    maximumAlnScore.update({((0, m), (-5, (0, m - 1))) for m in range(1, protein_t + 1)})

    for m,n in product(range(1,protein_s+1),range(1,protein_t+1)):
        cost = blosum62.get((s[m-1],t[n-1]))
        if cost == None:
            cost = blosum62.get((t[n-1],s[m-1]))
        a[(m, n)] = maximumAlnScore[(m-1,n-1)][0] + cost
        b[(m, n)] =max(maximumAlnScore[(m - 1, n)][0] - 5,b.get((m-1,n)))
        c[(m, n)] = max(maximumAlnScore[(m, n - 1)][0] - 5, c.get((m, n-1)))

        score = max(a[(m, n)],b[(m, n)],c[(m, n)])
        if score == a[(m, n)]:
            maximumAlnScore[(m, n)] = (score,(m-1, n-1))
        elif score == b[(m, n)]:
            maximumAlnScore[(m, n)] = (score,(m-1, n))
        elif score == c[(m, n)]:
            maximumAlnScore[(m, n)] = (score,(m, n-1))
    return maximumAlnScore[(m, n)][0]


if __name__ == '__main__':
    line_count = 0
    s_prot = []
    t_prot = []
    proteinStrFile = open('C:/Users/Rajesh/PycharmProjects/GlobAligConstGapPb34/rosalind_gcon.txt', 'r')
    for line in proteinStrFile:
        if line.startswith('>'):
            line_count += 1
            continue
        elif line_count == 1:
            for l in line.strip('\n'):
                s_prot.append(l)
        else:
            for m in line.strip('\n'):
                t_prot.append(m)

    print s_prot
    print t_prot
    print globAlign(s_prot,t_prot)


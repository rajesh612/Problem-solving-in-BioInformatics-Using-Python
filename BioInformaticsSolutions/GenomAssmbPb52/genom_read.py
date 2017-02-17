dna_str = "ACGT"
comp_dict = {"A": "T", "C": "G", "T": "A", "G": "C"}


def get_comp(dna):
    comp = ""

    for i in range(len(dna)):
        comp = comp_dict[dna[i]] + comp

    return comp

if __name__ == '__main__':
    strg = [x.strip() for x in open('C:/Users/Rajesh/PycharmProjects/GenomAssmbPb52/rosalind_gasm.txt').readlines()]

    for k in reversed(range(2, len(strg[0]) + 1)):
        kmers = set()

        for s in strg:
            for i in range(len(s) - k + 1):
                kmers.add(s[i:i + k])
                kmers.add(get_comp(s[i:i + k]))

        sup_str = None

        stack = []
        stack.append(([], set()))

        while len(stack) > 0 and sup_str == None:
            path, vs = stack.pop()

            if len(path) == 0:
                for kmer in kmers:
                    stack.append(([kmer], set([kmer])))
            else:
                mer = path[-1]

                for a in dna_str:
                    nmer = mer[1:] + a

                    if nmer in kmers and nmer != get_comp(kmer):
                        if nmer == path[0]:
                            sup_str = list(path)
                            break
                        elif not nmer in vs:
                            stack.append((path + [nmer], vs.union(set([nmer]))))

        if sup_str != None:
            cyclic_str = sup_str[0]

            for i in range(1, len(sup_str)):
                cyclic_str += sup_str[i][-1]

            cyclic_str = cyclic_str[:-(k - 1)]
            doutput = cyclic_str + cyclic_str
            success = True

            for dna in strg:
                if doutput.find(dna) == -1 and doutput.find(get_comp(dna)) == -1:
                    success = False

            if success:
                print cyclic_str
                break

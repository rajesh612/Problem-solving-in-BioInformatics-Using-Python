# user defined module
import nwick

def dist(s, t):
    ret = 0

    for k in range(len(s)):
        if s[k] != t[k]:
            ret += 1

    return ret


def parse(s):
    s = s.strip()
    lines = s.split()
    dna_dict = {}
    ckey = ""
    key_seq = []

    for line in lines:
        if line[0] == ">":
            ckey = line[1:]
            key_seq.append(ckey)
            dna_dict[ckey] = ""
        else:
            dna_dict[ckey] += line

    return dna_dict, key_seq


if __name__ == "__main__":
    internal = []
    dna_alpha = "ACGT-"

    with open("C:/Users/Rajesh/PycharmProjects/AlgnPylPb37/rosalind_alph.txt") as input_file:
        btree = input_file.readline()
        fasta = input_file.read()
        btree = btree.strip()

    tree = nwick.nwk_parse(btree)
    dnas, key = parse(fasta)

    adj_list, child = tree.adj_list()
    ordered = tree.level_traverse()

    assert (set(ordered) == set(tree.taxa()))

    for taxon in ordered:
        if tree.u != taxon:
            assert (len(adj_list[taxon]) == len(child[taxon]) + 1)
        else:
            assert (len(adj_list[taxon]) == len(child[taxon]))

        if len(adj_list[taxon]) > 1:
            internal.append(taxon)

    for taxon in ordered:
        for c in child[taxon]:
            assert (ordered.index(c) < ordered.index(taxon))

    dp, pre = {}, {}
    l = len(dnas[key[0]])

    for k in range(l):
        dp[k] = {}
        pre[k] = {}

        for taxon in internal:
            dp[k][taxon] = {}
            pre[k][taxon] = {}

            for a in dna_alpha:
                dp[k][taxon][a] = 0
                pre[k][taxon][a] = {}

                for c in child[taxon]:
                    if len(child[c]) == 0:  # leaf node
                        if a != dnas[c][k]:
                            dp[k][taxon][a] += 1

                        pre[k][taxon][a][c] = dnas[c][k]
                    else:  # another internal node
                        alpa_a = a
                        minc = 0

                        for b in dna_alpha:
                            if b == a:
                                inc = 0
                            else:
                                inc = 1

                            if dp[k][c][alpa_a] + minc > dp[k][c][b] + inc:
                                alpa_a = b
                                minc = inc

                        dp[k][taxon][a] += minc + dp[k][c][alpa_a]
                        pre[k][taxon][a][c] = alpa_a

    root = tree.u
    res = 0

    for k in range(l):
        res += min(dp[k][root].values())

    print(res)

    result = {}

    for k in range(l):
        def reconstruct_dna(node, a):
            result.setdefault(node, "")
            result[node] += a

            for c in child[node]:
                reconstruct_dna(c, pre[k][node][a][c])


        ra = min(dp[k][root], key=dp[k][root].get)
        reconstruct_dna(root, ra)

    for key, val in result.items():
        if key in internal:
            print(">%s" % key)
            print(val)

    ch = 0

    for taxon in ordered:
        for c in child[taxon]:
            ch += dist(result[taxon], result[c])

    assert (ch == res)
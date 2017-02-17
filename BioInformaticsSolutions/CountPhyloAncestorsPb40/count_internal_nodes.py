if __name__ == '__main__':
    internal_nodes = 0
    n_val = open('C:/Users/Rajesh/PycharmProjects/CountPhyloAncestorsPb40/rosalind_unrttree.txt', 'r')
    for leaves in n_val:
        internal_nodes = int(leaves) - 2
    print internal_nodes

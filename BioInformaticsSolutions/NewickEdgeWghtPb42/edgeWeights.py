# Distance between two nodes in a Weighted Tree
from StringIO import StringIO
from Bio import Phylo

if __name__ == '__main__':
    distance_result = []
    pair_lines =[]
    weighted_tree_file = open('C:/Users/Rajesh/PycharmProjects/NewickEdgeWghtPb42/rosalind_nkew.txt').read().strip().split('\n\n')
    pair_lines= [line.split('\n') for line in weighted_tree_file]
    print pair_lines
    for tree, node_pair in pair_lines:
        u,v = node_pair.split()
        # Phylo.read() will get the information of tree in newick format
        tree_nodes = Phylo.read(StringIO(tree),'newick')
        node_distance = tree_nodes.distance(u,v)
        distance_result.append(int(node_distance))

    print(' '.join(str(dist) for dist in distance_result))

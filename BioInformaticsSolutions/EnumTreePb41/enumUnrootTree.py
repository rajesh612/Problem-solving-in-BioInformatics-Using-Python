class Edge():
    def __init__(self, l_node, r_node):
        self.nodes = [l_node, r_node]

    def __str__(self):
        return "{}--{}".format(*self.nodes)

class Node():
    def __init__(self, node_name):
        self.node_name = node_name

    def __str__(self):
        if self.node_name is not None:
            return self.node_name
        else:
            return "internal_node_{}".format(id(self))

class UnrootedBTree():
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def __str__(self):
        return "tree_{} edges: {}".format(id(self), [str(x) for x in self.edges])

    def cc_tree(self):
        alter_node = {node: Node(node.node_name) for node in self.nodes}
        new_nodes = list(alter_node.values())
        new_edges = [Edge(alter_node[edge.nodes[0]], alter_node[edge.nodes[1]]) for edge in self.edges]

        new_tree = UnrootedBTree(new_nodes, new_edges)
        return new_tree

def enum_unrooted_trees(species):
    assert(len(species) > 1)
    if len(species) == 2:
        n1, n2 = species
        t = UnrootedBTree()
        t.nodes = [Node(n1), Node(n2)]
        t.edges = [Edge(t.nodes[0], t.nodes[1])]
        return [t]
    elif len(species) > 2:
    # get the smaller tree first
      old_trees = enum_unrooted_trees(species[:-1])
      new_species_name = species[-1]
      new_trees = []

    for old_tree in old_trees:
      for i in range(len(old_tree.edges)):
        new_tree = old_tree.cc_tree()
        edge_to_split = new_tree.edges[i]
        old_l_node, old_r_node = edge_to_split.nodes

        # remove the old edge
        new_tree.edges.remove(edge_to_split)

        # add a new internal_node node
        internal_node = Node(None)
        new_tree.nodes.append(internal_node)

        # add new species
        new_species = Node(new_species_name)
        new_tree.nodes.append(new_species)

        # add three new edges
        new_tree.edges.append(Edge(old_l_node, internal_node))
        new_tree.edges.append(Edge(old_r_node, internal_node))
        new_tree.edges.append(Edge(new_species, internal_node))

        # append new tree in the list
        new_trees.append(new_tree)

    return new_trees

def enumeration(tree_input):
  tree = tree_input.cc_tree()

  if len(tree.nodes) == 1:
    return "{};".format(tree.nodes[0])
  elif len(tree.nodes) == 2:
    return "({},{});".format(*tree.nodes)
  elif len(tree.nodes) > 2:
    for child_node in tree.nodes:
      # ignore species
      if child_node.node_name is not None:
        continue

      neighbor_edges = [edge for edge in tree.edges if child_node in edge.nodes]
      neighbor_nodes = [node for edge in neighbor_edges for node in edge.nodes if node in edge.nodes and node is not child_node]
      neighbor_species = [node for node in neighbor_nodes if node.node_name is not None]

      # find a node with two species
      if len(
                neighbor_species) == 2 or len(
                neighbor_species) == 3:
        species1, species2 = neighbor_species[0: 2]
        edges_to_cut = [edge for
                edge in neighbor_edges if species1 in edge.nodes or species2

                in edge.nodes]
        child_node.node_name = "({},{})".format(species1, species2)
        # remove species
        tree.nodes.remove(species1)
        tree.nodes.remove(species2)
        for edge in edges_to_cut:tree.edges.remove(edge)
        return enumeration(tree)

if __name__ == '__main__':
    species = open('C:/Users/Rajesh/PycharmProjects/EnumTreePb41/rosalind_eubt.txt').read().split()
    trees = enum_unrooted_trees(species)
    print '\n'.join([enumeration(tree) for tree in trees])
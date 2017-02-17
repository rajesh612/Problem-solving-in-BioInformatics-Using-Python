from itertools import count

class RootedTrie(object):
    def __init__(self):
        self.counter = count(start=1)
        self.root = [next(self.counter), {}]

    def fill_in(self, parent):
        node = self.root
        for child in parent:
            if child not in node[1]:
                node[1][child] = [next(self.counter), {}]

            node = node[1][child]

def list(strings):
    root_trie = RootedTrie()
    for string in strings:
        root_trie.fill_in(string)
    return root_trie.root

def result(node):
    for child, node2 in node[1].iteritems():
        print node[0], node2[0], child
        result(node2)

if __name__ == '__main__':
    dna_strings = open('C:/Users/Rajesh/PycharmProjects/PatternmatchPb18/trei.txt').readlines()
    dna_strings = [s.strip() for s in dna_strings if s.strip()]

    result(list(dna_strings))
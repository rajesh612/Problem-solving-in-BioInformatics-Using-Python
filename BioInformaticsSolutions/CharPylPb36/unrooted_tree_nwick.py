# user defined module
import nwick

class Node:
    def __init__(self, taxon=None):
        self.adjs = set()

        for adj in self.adjs:
            adj.add_adj(self)

        self.taxon = taxon

    def add_adj(self, branch):
        self.adjs.add(branch)

        if not branch.is_adj(self):
            branch.add_adj(self)

    def prune(self, branchs):
        self.adjs = self.adjs.difference(set(branchs))

        for branch in branchs:
            if branch.is_adj(self):
                branch.prune([self])

    def fold(self, par=None):
        # Internal node
        if self.taxon == None:
            ret = ",".join([adj.fold(self) for adj in self.adjs if adj != par])

            if ret != "":
                ret = "(" + ret + ")"
        else:  # Taxon node
            ret = self.taxon

        return ret

    def taxa(self, par=None, ret=None):
        if ret == None:
            ret = set()

        if self.taxon != None:
            ret.add(self.taxon)

        for adj in self.adjs:
            if adj != par:
                ret = adj.taxa(self, ret)

        return ret

    def split(self, cat):
        branches = set()
        subtaxa_branch = set()

        for adj in self.adjs:
            subtaxa = adj.taxa(self)

            if subtaxa.issubset(cat):
                branches.add(adj)
                subtaxa_branch = subtaxa_branch.union(subtaxa)
            elif len(subtaxa.intersection(cat)) > 0:
                return False

        if subtaxa_branch == cat:
            ni = Node()
            internals.append(ni)

            self.prune(branches)
            self.add_adj(ni)

            for b in branches:
                ni.add_adj(b)

            return True

        return False

    def is_internal(self):
        return self.taxon == None

    def is_adj(self, branch):
        return branch in self.adjs

    def __str__(self):
        if self.is_internal():
            return str([adj.taxon for adj in self.adjs])

        return str(self.taxon)

    def __repr__(self):
        return "taxon:" + str(self)

    def check_struct(self):
        for adj in self.adjs:
            assert (self in adj.adjs)


def init_taxa(taxa):
    global internals

    root = Node()
    internals = []

    internals.append(root)
    for taxon in taxa:
        root.add_adj(Node(taxon))


def split(char, taxa):
    cat = set()
    for i in range(len(taxa)):
        if char[i] == "0":
            cat.add(taxa[i])

    success = False
    for n in internals:
        if n.split(cat):
            success = True
            break

    return success


def rev(s):
    ret_data = ""
    for i in range(len(s)):
        if s[i] == "0":
            ret_data += "1"
        else:
            ret_data += "0"

    return ret_data


def gen_char(cat, taxa):
    ret = ""
    for i in range(len(taxa)):
        if taxa[i] in cat:
            ret += "1"
        else:
            ret += "0"

    return ret


def consistent(chars, taxa):
    init_taxa(taxa)

    for char in chars:
        if not split(char, taxa):
            return False

    return True


if __name__ == '__main__':
    internals = []

    with open('C:/Users/Rajesh/PycharmProjects/CharPylPb36/rosalind_chbp.txt') as in_file:
        line = in_file.readline()
        line = line.strip()
        taxa = line.split()

        init_taxa(taxa)

        chars = []

        charec = in_file.readline()
        charec = charec.strip()

        while charec != "":
            split(charec, taxa)
            chars.append(charec)

            charec = in_file.readline()
            charec = charec.strip()

    r = internals.pop()
    output = r.fold() + ";"

    t = nwick.nwk_parse(output)
    r = nwick.edg_split(t, taxa)

    for charec in chars:
        assert (charec in r or rev(charec) in r)

    print output
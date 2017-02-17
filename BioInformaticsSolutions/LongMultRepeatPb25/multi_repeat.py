class Node:
    def __init__(self, label):
        self.f = self.t = 0
        self.s = set()
        self.label = label

    def __repr__(self):
        return '%s(f=%s, t=%s, s=%s)' % tuple(map(str, (self.label, self.f, self.t, self.s)))


def get_mul_repeat(r, l):
    global long_len, long_str
    substr = 0

    if r.t == len(s):
        return 1

    str_list.append((r.f, r.t))

    for son in r.s:
        substr += get_mul_repeat(son, l + r.t - r.f)

    if substr >= k and l + r.t - r.f > long_len:
        long_str = list(str_list)
        long_len = l + r.t - r.f

    str_list.pop()

    return substr


if __name__ == '__main__':
    child = set()
    nodes = {}
    long_len = 0
    long_str = []
    str_list = []

    with open('C:/Users/Rajesh/PycharmProjects/LongMultRepeatPb25/rosalind_lrep.txt') as dna_file:
        s = dna_file.readline().strip()
        k = int(dna_file.readline().strip())

        for edge_list in map(str.strip, dna_file.readlines()):
            parent_label, child_label, sub_loc, t_len = edge_list.split()

            parent_node = nodes.setdefault(parent_label, Node(parent_label))
            child_node = nodes.setdefault(child_label, Node(child_label))
            child_node.f = int(sub_loc) - 1
            child_node.t = int(sub_loc) + int(t_len) - 1

            parent_node.s.add(child_node)
            child.add(child_node)

        root_node = (set(nodes.values()) - child).pop()

    get_mul_repeat(root_node, 0)

    print ''.join(s[i:j] for (i, j) in long_str)

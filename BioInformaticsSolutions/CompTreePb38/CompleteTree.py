if __name__ == '__main__':
    tree_count = 0
    branch_count = 0
    min_edges = 0
    string_seq = open('C:/Users/Rajesh/PycharmProjects/CompTreePb38/rosalind_tree.txt', 'r')
    for line in string_seq:
        if tree_count == 0:
            tree_count = int(line)
            branch_count +=1
        else:
            branch_count +=1

    min_edges = tree_count - branch_count
    print min_edges
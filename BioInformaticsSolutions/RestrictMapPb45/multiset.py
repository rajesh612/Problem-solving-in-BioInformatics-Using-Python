from collections import Counter

def get_restrict_map(data):
    # Initialize variables.
    x = {0}
    max_set = max(data)

    # Create lambda functions for multiset operations.
    new_data = lambda y, S: Counter(abs(y-s) for s in S)
    filt_data = lambda a, b: all(a[i] <= b[i] for i in a)

    # Create the multiset
    while len(data) > 0:
        y = max(data)
        if filt_data(new_data(y, x), data):
            x |= {y}
            data -= new_data(y, x)
        else:
            x |= {max_set - y}
            data -= new_data(max_set - y, x)

    return x

if __name__ == '__main__':
    multiset_file = open('C:/Users/Rajesh/PycharmProjects/RestrictMapPb45/rosalind_pdpl.txt')
    multiset_data = Counter(map(int,multiset_file.read().strip().split()))

    x = sorted(list(get_restrict_map(multiset_data)))

    print ' '.join(map(str, x))

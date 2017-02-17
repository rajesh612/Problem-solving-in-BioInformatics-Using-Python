def get_str(bwt_in):
    enum_bwt = enum_text(bwt_in)
    enum_sort_bwt = enum_text(sorted(bwt_in))

    # dicionary between enumerated BWT and sorted bwt.
    inverse_dict = {enum_bwt[i]: enum_sort_bwt[i] for i in xrange(len(bwt))}

    inverse_bwt = ''
    current_char = enum_bwt[0]
    for i in xrange(len(bwt)):
        current_char = inverse_dict[current_char]
        inverse_bwt += current_char[0]

    return inverse_bwt[1:] + inverse_bwt[0]


def enum_text(text):

    # Initialize the string count and enumerated character list.
    str_count = {}
    list_str = []

    # Enumerate like characters.
    for t in text:
        if t not in str_count:
            str_count[t] = 0
        else:
            str_count[t] += 1
        list_str.append(t + str(str_count[t]))

    return list_str


if __name__ == "__main__":
    bwt_file = open('C:/Users/Rajesh/PycharmProjects/StringFromBWPb50/bwtfile.txt')
    bwt = bwt_file.read().strip()
    print get_str(bwt)

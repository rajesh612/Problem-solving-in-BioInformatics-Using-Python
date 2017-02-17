def lis(lis_seq):
    """Returns the longest increasing sequence from input file"""
    seq_length = len(lis_seq)
    p = [0] * seq_length
    m = [0] * (seq_length + 1)
    seq_line = 0
    for i in range(seq_length):
        low = 1
        hi = seq_line
        while low <= hi:
            mid = (low + hi) // 2
            if lis_seq[m[mid]] < lis_seq[i]:
                low = mid + 1
            else:
                hi = mid - 1

        new_seq_line = low
        p[i] = m[new_seq_line - 1]
        m[new_seq_line] = i

        if (new_seq_line > seq_line):
            seq_line = new_seq_line

    S = []
    k = m[seq_line]
    for i in range(seq_line - 1, -1, -1):
        S.append(lis_seq[k])
        k = p[k]
    return S[::-1]


def lds(lds_seq):
    """Returns the longest decreasing sequence from input file"""
    m = [0] * len(lds_seq)
    for x in range(len(lds_seq) - 2, -1, -1):
        for y in range(len(lds_seq) - 1, x, -1):
            if m[x] <= m[y] and lds_seq[x] > lds_seq[y]:
                m[x] = m[y] + 1  # or use m[x]+=1
    max_value = max(m)

    lds_result = []
    for i in range(len(m)):
        if max_value == m[i]:
            lds_result.append(lds_seq[i])
            max_value -= 1

    return lds_result

if __name__ == '__main__':
    int_lis_seq = []
    int_lds_seq = []
    seq = open('rosalind_lgis.txt', 'r')
    for line in seq:
        l = line.split()
        if len(l) != 1:
            for k in l:
                int_lis_seq.append(int(k))

            with open('problem23out.txt', 'w') as output_data:
                output_data.write(' '.join(map(str, lis(int_lis_seq))))
                output_data.write("\n")
            for j in l:
                int_lds_seq.append(int(j))

            with open('problem23out.txt', 'a') as output_data:
                output_data.writelines(' '.join(map(str, lds(int_lds_seq))))
        else:
            continue




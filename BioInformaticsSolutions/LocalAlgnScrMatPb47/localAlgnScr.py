def pam250_scr_mat(u, w):
    p = 0
    q = 0

    if u == 'A': p = 0
    if u == 'R': p = 1
    if u == 'N': p = 2
    if u == 'D': p = 3
    if u == 'C': p = 4
    if u == 'Q': p = 5
    if u == 'E': p = 6
    if u == 'G': p = 7
    if u == 'H': p = 8
    if u == 'I': p = 9
    if u == 'L': p = 10
    if u == 'K': p = 11
    if u == 'M': p = 12
    if u == 'F': p = 13
    if u == 'P': p = 14
    if u == 'S': p = 15
    if u == 'T': p = 16
    if u == 'W': p = 17
    if u == 'Y': p = 18
    if u == 'V': p = 19

    if w == 'A': q = 0
    if w == 'R': q = 1
    if w == 'N': q = 2
    if w == 'D': q = 3
    if w == 'C': q = 4
    if w == 'Q': q = 5
    if w == 'E': q = 6
    if w == 'G': q = 7
    if w == 'H': q = 8
    if w == 'I': q = 9
    if w == 'L': q = 10
    if w == 'K': q = 11
    if w == 'M': q = 12
    if w == 'F': q = 13
    if w == 'P': q = 14
    if w == 'S': q = 15
    if w == 'T': q = 16
    if w == 'W': q = 17
    if w == 'Y': q = 18
    if w == 'V': q = 19

    pam250_mat = [[2, -2, 0, 0, -2, 0, 0, 1, -1, -1, -2, -1, -1, -3, 1, 1, 1, -6, -3, 0],
              [-2, 6, 0, -1, -4, 1, -1, -3, 2, -2, -3, 3, 0, -4, 0, 0, -1, 2, -4, -2],
              [0, 0, 2, 2, -4, 1, 1, 0, 2, -2, -3, 1, -2, -3, 0, 1, 0, -4, -2, -2],
              [0, -1, 2, 4, -5, 2, 3, 1, 1, -2, -4, 0, -3, -6, -1, 0, 0, -7, -4, -2],
              [-2, -4, -4, -5, 12, -5, -5, -3, -3, -2, -6, -5, -5, -4, -3, 0, -2, -8, 0, -2],
              [0, 1, 1, 2, -5, 4, 2, -1, 3, -2, -2, 1, -1, -5, 0, -1, -1, -5, -4, -2],
              [0, -1, 1, 3, -5, 2, 4, 0, 1, -2, -3, 0, -2, -5, -1, 0, 0, -7, -4, -2],
              [1, -3, 0, 1, -3, -1, 0, 5, -2, -3, -4, -2, -3, -5, 0, 1, 0, -7, -5, -1],
              [-1, 2, 2, 1, -3, 3, 1, -2, 6, -2, -2, 0, -2, -2, 0, -1, -1, -3, 0, -2],
              [-1, -2, -2, -2, -2, -2, -2, -3, -2, 5, 2, -2, 2, 1, -2, -1, 0, -5, -1, 4],
              [-2, -3, -3, -4, -6, -2, -3, -4, -2, 2, 6, -3, 4, 2, -3, -3, -2, -2, -1, 2],
              [-1, 3, 1, 0, -5, 1, 0, -2, 0, -2, -3, 5, 0, -5, -1, 0, 0, -3, -4, -2],
              [-1, 0, -2, -3, -5, -1, -2, -3, -2, 2, 4, 0, 6, 0, -2, -2, -1, -4, -2, 2],
              [-3, -4, -3, -6, -4, -5, -5, -5, -2, 1, 2, -5, 0, 9, -5, -3, -3, 0, 7, -1],
              [1, 0, 0, -1, -3, 0, -1, 0, 0, -2, -3, -1, -2, -5, 6, 1, 0, -6, -5, -1],
              [1, 0, 1, 0, 0, -1, 0, 1, -1, -1, -3, 0, -2, -3, 1, 2, 1, -2, -3, -1],
              [1, -1, 0, 0, -2, -1, 0, 0, -1, 0, -2, 0, -1, -3, 0, 1, 3, -5, -3, 0],
              [-6, 2, -4, -7, -8, -5, -7, -7, -3, -5, -2, -3, -4, 0, -6, -2, -5, 17, 0, -6],
              [-3, -4, -2, -4, 0, -4, -4, -5, 0, -1, -1, -4, -2, 7, -5, -3, -3, 0, 10, -2],
              [0, -2, -2, -2, -2, -2, -2, -1, -2, 4, 2, -2, 2, -1, -1, -1, 0, -6, -2, 4]]

    return pam250_mat[p][q]


def zeros(k):
    return_val = []
    for _ in range(k[0]):
        return_val.append([])
        for _ in range(k[1]):
            return_val[-1].append(0)
    return return_val


def matched_score(x, y):
    if x == '-' or y == '-':
        return linear_gap
    else:
        return pam250_scr_mat(x, y)


def opt_score(alignment1, alignment2):
    i, score = 0, 0
    symbol = ''

    for i in range(0, len(alignment1)):
        # if two AAs are the same, then output the letter
        if alignment1[i] == alignment2[i]:
            symbol = symbol + alignment1[i]
            score += matched_score(alignment1[i], alignment2[i])

        # if they are not identical and none of them is gap
        elif alignment1[i] != alignment2[i] and alignment1[i] != '-' and alignment2[i] != '-':
            score += matched_score(alignment1[i], alignment2[i])
            symbol += ' '

        # if one of them is a gap, output a space
        elif alignment1[i] == '-' or alignment2[i] == '-':
            symbol += ' '
            score += linear_gap

    print score
    print alignment1.replace("-", "")
    print alignment2.replace("-", "")


def max_algn_score(s_str, t_str):
    a, b = len(s_str), len(t_str)

    opt_algn_score = zeros((a + 1, b + 1))
    traceback = zeros((a + 1, b + 1))
    max_score = 0

    for i in range(1, a + 1):
        for j in range(1, b + 1):
            diag_score = opt_algn_score[i - 1][j - 1] + matched_score(s_str[i - 1], t_str[j - 1])
            top = opt_algn_score[i][j - 1] + linear_gap
            left = opt_algn_score[i - 1][j] + linear_gap
            opt_algn_score[i][j] = max(0, left, top, diag_score)

            if opt_algn_score[i][j] == diag_score:
                traceback[i][j] = 3  # 3 to trace diagonal
            if opt_algn_score[i][j] == top:
                traceback[i][j] = 2  # 2 to trace left
            if opt_algn_score[i][j] == left:
                traceback[i][j] = 1  # 1 to trace up
            if opt_algn_score[i][j] == 0:
                traceback[i][j] = 0  # 0 to end of the path
            if opt_algn_score[i][j] >= max_score:
                max_i = i
                max_j = j
                max_score = opt_algn_score[i][j];

    alignment1, alignment2 = '', ''

    i = max_i
    j = max_j

    while traceback[i][j] != 0:
        if traceback[i][j] == 3:
            alignment1 = s_str[i - 1] + alignment1
            alignment2 = t_str[j - 1] + alignment2
            i -= 1
            j -= 1
        elif traceback[i][j] == 2:
            alignment1 = '-' + alignment1
            alignment2 = t_str[j - 1] + alignment2
            j -= 1
        elif traceback[i][j] == 1:
            alignment1 = s_str[i - 1] + alignment1
            alignment2 = '-' + alignment2
            i -= 1

    opt_score(alignment1, alignment2)


if __name__ == '__main__':
    fasta_lines = 0
    s = []
    t = []
    proteinFile = open('C:/Users/Rajesh/PycharmProjects/LocalAlgnScrMatPb47/rosalind_local.txt', 'r')
    for line in proteinFile:
        if line.startswith('>'):
            fasta_lines += 1
            continue
        elif fasta_lines == 1:
            for l in line.strip('\n'):
                s.append(l)
        else:
            for m in line.strip('\n'):
                t.append(m)

    linear_gap = -5
    max_algn_score(s, t)
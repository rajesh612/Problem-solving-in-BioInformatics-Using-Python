def edit_dist(s, t):
    rows = len(t) + 1
    colms = len(s) + 1
    dist_array = [[0 for i in range(colms)] for j in range(rows)]
    # first column of distance array
    for m in range(1, rows):
        dist_array[m][0] = m

    # first row of distance array
    for n in range(1, colms):
        dist_array[0][n] = n

    for row in range(1, rows):
        for colm in range(1, colms):
            if s[colm - 1] == t[row - 1]:
                dist_array[row][colm] = dist_array[row - 1][colm - 1]
            else:
                dist_array[row][colm] = min(dist_array[row - 1][colm - 1] + 1, dist_array[row - 1][colm] + 1,
                                            dist_array[row][colm - 1] + 1)

    return dist_array[row][colm]


if __name__ == '__main__':
    s = []
    t = []
    string_seq = open('C:/Users/Rajesh/PycharmProjects/EditDistProb30/rosalind_edit.txt', 'r')
    for line in string_seq:
        if line.startswith('>'):
            continue
        else:
            l = line.strip()
            if len(s) == 0:
                for x in l:
                    s.append(x)
            else:
                for y in l:
                    t.append(y)
    print(s)
    print(t)
    print(edit_dist(s, t))
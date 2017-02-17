def align_matrix(protein_s, protein_t):
    align_dict = {
    (m, n): (n + m + 2, (max(m - 1, -1), max(n - 1, -1), (protein_s[m] if m >= 0 else '-'), (protein_t[n]) if n >= 0 else '-')) for m in range(-1, len(protein_s)) for n in range(-1, len(protein_t))}
    align_dict[-1, -1] = (0, (-1, -1, '', ''))

    [optimal_alignment(align_dict, m, n) for m in range(len(protein_s)) for n in range(len(protein_t))]

    return align_dict

def optimal_alignment(align_dict, m, n):
    m_gap = (align_dict[m - 1, n][0] + 1, (m - 1, n, protein_s[m], "-"))
    n_gap = (align_dict[m, n - 1][0] + 1, (m, n - 1, "-", protein_t[n]))
    no_gap = (align_dict[m - 1, n - 1][0] + int(protein_s[m] != protein_t[n]), (m - 1, n - 1, protein_s[m], protein_t[n]))

    align_dict[m, n] = min(m_gap, n_gap, no_gap)


def edit_distance(aligned_matrix,protein_s, protein_t):
    mat = aligned_matrix[len(protein_s) - 1, len(protein_t) - 1]
    max_gap = mat[0]
    s_augmt = [mat[1][2]]
    t_augmt = [mat[1][3]]

    while (mat[1][2], mat[1][3]) != ('', ''):
        mat = aligned_matrix[mat[1][0], mat[1][1]]
        s_augmt.append(mat[1][2])
        t_augmt.append(mat[1][3])

    return (max_gap, "".join(s_augmt[::-1]), "".join(t_augmt[::-1]))


if __name__ == "__main__":
    s_t_count = 0
    protein_s = []
    protein_t = []
    proteinStrFile = open('C:/Users/Rajesh/PycharmProjects/EditDistAlignPb31/rosalind_edta.txt', 'r')
    for line in proteinStrFile:
        if line.startswith('>'):
            s_t_count +=1
            continue
        elif s_t_count == 1:
            for l in line.strip('\n'):
                protein_s.append(l)
        else:
            for l in line.strip('\n'):
                protein_t.append(l)
    aligned_matrix= align_matrix(protein_s, protein_t)
    distance, augmented_s, augmented_t = edit_distance(aligned_matrix,protein_s, protein_t)

    print distance,'\n', augmented_s,'\n', augmented_t
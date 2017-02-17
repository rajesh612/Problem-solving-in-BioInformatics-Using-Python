from Bio import SeqIO

def profile(list_arr):
    profile_matrix = [[0 for j in range(len(list_arr[0]))] for i in range(4)]
    for row in range(len(list_array)):
        for col in range(len(list_array[row])):
            if list_array[row][col] == 'A':
                profile_matrix[0][col] += 1
            elif list_array[row][col] == 'C':
                profile_matrix[1][col] += 1
            elif list_array[row][col] == 'G':
                profile_matrix[2][col] += 1
            elif list_array[row][col] == 'T':
                profile_matrix[3][col] += 1
    return profile_matrix

def print_profile(pf_result):
    profile_mat = pf_result
    for i in range(len(profile_mat)):
        if i == 0:
            profile_mat[i].insert(0,"A: ")
        elif i == 1:
            profile_mat[i].insert(0,"C: ")
        elif i == 2:
            profile_mat[i].insert(0,"G: ")
        elif i == 3:
            profile_mat[i].insert(0,"T: ")
    for x in profile_mat:
        temp_profile = []
        for y in x:
            temp_profile.append(y)
        with open('C:/Users/Rajesh/PycharmProjects/ProfileConsenProb24/problem24out.txt', 'a') as output_data:
            output_data.writelines(' '.join(map(str, temp_profile)))
            output_data.writelines("\n")
        del temp_profile



def consensus(result_mat):
    profile_matrix = result_mat
    consensus_mat = []
    for m in range(len(profile_matrix[0])):
        mode = 0
        index = 0
        for n in range(len(profile_matrix)):
            if profile_matrix[n][m] > mode:
                mode = profile_matrix[n][m]
                index = n
        if index == 0:
            consensus_mat.append('A')
        elif index == 1:
            consensus_mat.append('C')
        elif index == 2:
            consensus_mat.append('G')
        elif index == 3:
            consensus_mat.append('T')
    return consensus_mat



if __name__ == '__main__':
    list_array = []
    for record in SeqIO.parse("C:/Users/Rajesh/PycharmProjects/ProfileConsenProb24/rosalind_cons.txt", "fasta"):
        list_array.append(str(record.seq))

    result = profile(list_array)

    with open('C:/Users/Rajesh/PycharmProjects/ProfileConsenProb24/problem24out.txt', 'w') as output_data:
        output_data.write(''.join(map(str,consensus(result))))
        output_data.writelines("\n")

    print_profile(result)




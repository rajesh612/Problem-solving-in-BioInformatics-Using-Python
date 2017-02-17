if __name__ == '__main__':
    s_array = []
    t_array =[]
    hamm_dist = 0
    hamm_file = open('C:/Users/Rajesh/PycharmProjects/HammDistProb29/rosalind_hamm.txt','r')
    for line in hamm_file:
        clean_line = line.strip()
        if len(s_array) == 0:
            for s_char in clean_line:
                s_array.append(str(s_char))
        else:
            for t_char in clean_line:
                t_array.append(str(t_char))

    for l in range(len(s_array)):
        if s_array[l] == t_array[l]:
            continue
        else:
            hamm_dist +=1
    print hamm_dist





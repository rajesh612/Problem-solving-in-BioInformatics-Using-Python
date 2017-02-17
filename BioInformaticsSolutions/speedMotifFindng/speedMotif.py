def failure_array(s):
    i = -1
    p =[i]

    for index,k in enumerate(s):
        while i >= 0 and s[i] != k:
            i = p[i]

        i += 1
        p.append(i)
    return p[1:]



if __name__ == "__main__":
    s = open('rosalind_kmp.txt','r')
    line_join = ""
    for line in s:
        if line.startswith('>'):
            continue
        else:
            line = line.strip()
            line_join += line
    failure_arr = failure_array(line_join)
    with open('problem22op.txt', 'w') as output_data:
        output_data.write(' '.  join(map(str, failure_arr)))


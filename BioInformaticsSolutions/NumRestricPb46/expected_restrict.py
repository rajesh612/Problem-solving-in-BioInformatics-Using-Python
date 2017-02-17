from collections import Counter
from numpy import log, exp

if __name__ == "__main__":
    input_file = open("C:/Users/Rajesh/PycharmProjects/NumRestricPb46/rosalind_eval.txt").read().strip().split('\n')
    n = int(input_file[0])
    s = input_file[1]
    list_a = [float(i) for i in input_file[2].split()]
    dna = Counter(s)

    for num_a in list_a:
        b = (dna['A'] + dna['T']) * log((1 - num_a)/2) + (dna['G'] + dna['C']) * log(num_a / 2)
        b_list = exp(b) * (n - 1)
        print str(round(b_list,3)) ,
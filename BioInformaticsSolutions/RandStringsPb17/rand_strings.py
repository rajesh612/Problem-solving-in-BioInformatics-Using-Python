import math

def get_rand_strings(s,a):
    gc_content = s.count('G') + s.count('C')
    at_content = len(s) - gc_content
    for k in range(len(a)):
        b.append(math.log10((a[k] / 2) ** gc_content * (0.5 - a[k] / 2) ** at_content))

    return b

if __name__ == "__main__":
    b = []
    input_file = open('C:/Users/Rajesh/PycharmProjects/RandStringsPb17/rosalind_prob.txt', 'r')
    s = input_file.readline().strip()
    print s
    a = [float(k) for k in input_file.readline().split()]
    result = get_rand_strings(s,a)

    for i in range(len(result)):
      print round(result[i],3) ,


def mortal_rabbits(n_int, m_int, maturity=1):
    rabbit_pairs = []

    for k in range(n_int):
        if k < m_int:
            if k == 0 or k == 1:
                rabbit_pairs.append(1)
            else:
                rabbit_pairs.append(rabbit_pairs[-1] + rabbit_pairs[-2])
        else:
            num_rabbits = 0

            for l in range(k - m_int, k - maturity):
                num_rabbits = num_rabbits + rabbit_pairs[l]

            rabbit_pairs.append(num_rabbits)
    return rabbit_pairs

if __name__ == '__main__':
    fib_vars_file = open('C:/Users/Rajesh/PycharmProjects/RabbitFibonociPb16/rosalind_fibd.txt', 'r')
    n, m = fib_vars_file.readline().split()
    print mortal_rabbits(int(n), int(m))[-1]
def rabbit_pairs(i, j, k, n):
    total_rabbit_pairs = None
    if n == 1:
        total_rabbit_pairs = j
    else:
        total_rabbit_pairs = rabbit_pairs(j, i * k + j, k, n - 1)

    return total_rabbit_pairs

if __name__ == "__main__":
    n =0
    k =0
    fib_data = open('C:/Users/Rajesh/PycharmProjects/RabbitRecurrPb15/fib.txt','r')
    for line in fib_data:
        line = line.strip().split(' ')
        n = int(line[0])
        k = int(line[1])

print rabbit_pairs(0, 1, k, n)
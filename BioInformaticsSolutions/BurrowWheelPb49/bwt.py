
def bwt(text):
    text += ['', '$'][text[-1] != '$']

    L = len(text)

    # A lambda function to get the nth character of the cyclic rotation by i characters.
    rotat_index = lambda i, n: text[(n-i) % L]

    # Use the lambda function to compare rotation indices.
    comp_ind = lambda i, j, n=0: [1, -1][rotat_index(i,n) < rotat_index(j,n)] if rotat_index(i,n) != rotat_index(j,n) else comp_ind(i,j,n+1)

    # Sort the cyclic rotations
    sorted_str = sorted(xrange(len(text)), cmp=comp_ind)

    # Return the last index of each cyclic rotation
    return ''.join([rotat_index(i,-1) for i in sorted_str])

if __name__ == '__main__':
    with open('C:/Users/Rajesh/PycharmProjects/BurrowWheelPb49/inputstring.txt') as input_data:
        input_str = input_data.read().strip()

    print bwt(input_str)

'''
A program that explores DES concepts while not fully implementing des
'''


def shift_register(degree, xor_list):
    """
    Inputs:
    degree - the degree of shift register
    xor_list - a list defining where xors are

    decided to do this one by hand for now
    """
    pass

index_list = [31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 9, 10, 11, 12, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18, 19, 20, 19, 20, 21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31, 0]

key_a = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1]
key_b = [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1]
key_c = [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1]


def expand_key(s_box, key):
    """
    input:
    s_box - list of the order of indexes for output
    key - the input data

    output:
    a string representing the expanded key as a binary number
    """
    # create a list to append to for output
    output = []

    # iterate through sbox and append the corresponding indexes of key to output to expand
    for i in index_list:
        output.append(str(key[i]))

    # format to spec
    return "".join(output)


a = expand_key(index_list, key_a)
b = expand_key(index_list, key_b)
c = expand_key(index_list, key_c)

a_temp = "".join([str(i) for i in key_a])
b_temp = "".join([str(i) for i in key_b])
c_temp = "".join([str(i) for i in key_c])

print(f" S-Box as a list: {index_list}\n\n Problem a: key={ a_temp } and output={a}\n\n Problem b: key={b_temp} and output={b}\n\n Problem c: key={c_temp} and expanded key={c}\n\n")
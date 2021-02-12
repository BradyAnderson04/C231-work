"""
Contains methods for various ciphers -- viginere, ceazar
"""

'''
Reasoning:
n = 1
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B C D E F G H I J K L M N O P Q R S T U V W X Y Z A

n = 1
Hello drywall -> Ifmmp eszxbmm

process:
1.Convert string to ASCII
2.shift the letters
3.unshift letters

TODO:
1.Frequency analysis
2.vinginere cipher
'''

'''
Data cleaning:

1 - get a list of acceptable characters and loop through checking if they match

2 - use ascii values and if ascii values are not in acceptable range remove the value in question
    |-> I went with this method bc of it's simplicity and ease of implementation by using ascii values

'''

import random as rn
import math

# constants
KEY_LENGTH = 4


def convert_to_ascii(m):
    '''
    takes a message and makes it the equivalent ascii value

    inputs:
    m - string 
    output:
    list - a list of numbers
    '''
    # clean input to only be capital letters
    m = m.upper().replace(" ", "")

    # output storing
    ascii_list = []

    for i in range(len(m)):
        # remove any punctuation or other things we don't want
        temp = ord(m[i])
        # only append values from A - Z inc
        if(temp >= 65 and temp <=90):
            ascii_list.append(ord(m[i]))

    return ascii_list

def cipher_shift(n, ascii_list):
    """
    shift the cipher over n bits

    cipher - shifts n letters 

    65 - 90

    inputs:
    n - how many bits to shift by
    ascii_lits - list of ascii characters
    """
    shift_value = n%26 # 0 - 25

    output_ascii = [0] * len(ascii_list)

    for i in range(len(ascii_list)):
        temp = ascii_list[i] + shift_value

        if(temp > 90):
            # when greater than 90 subtract 26 - 
            temp -= 26
        if(temp < 65):
            # when you do a negative shift
            temp += 26

        output_ascii[i] = temp
    
    return output_ascii

def automate_ceasar_cipher(m, shift):
    ascii_list = convert_to_ascii(m)

    return cipher_shift(shift, ascii_list)

def display_cipher_shift(ascii_list):
    """
    shift the cipher over n bits

    cipher - shifts n letters 

    inputs:
    ascii_lits - list of ascii characters
    output:
    string representation
    """

    output = ""

    for i in ascii_list:
        output += chr(i)

    return output

def frequency_analysis(ascii_list):
    # create a histogram of the ascii list values
    freq_dict = {}

    for val in ascii_list:
        if(freq_dict.get(val) is not None):
            freq_dict[val] += 1 # increment value
        else:
            freq_dict[val] = 1 # create and init value

    return freq_dict

def display_dict(freq_dict):
    # iterate over keys and print the key value pair
    for key, val in freq_dict.items():
        print(key,":",val)

def v_cipher(key_size, message):
    '''
    iterate over key - execute cipher shift for key size bits of message

    ex: HELLOWORLD
    key = 3 long

    HEL LOW WOR LD_
    
    return the output message and shift values

    todo:

    program is not accurate there is a lengt of message difference
    '''
    # calc how many times a new key will be made
    print(len(message))
    loop_count = math.ceil(len(message) / key_size)

    output = [] # message encoded
    shift_outputs = [] # list of shift values
    
    for i in range(loop_count):
        # genearte a shift value
        temp_shift = rn.randint(0, 26) # generate val from 0 - 26 inc.
        # perform cipher shift on substring

        # define message substring to use
        bound_s = (i-1) * key_size
        bound_e = i * key_size
        m_sub = message[bound_s: bound_e]

        output_ascii = automate_ceasar_cipher(m_sub, temp_shift) # generate ascii of length key_size
        
        # save to output
        shift_outputs.append(temp_shift)
        [output.append(x) for x in output_ascii]
    
    # return output
    return output, shift_outputs

if __name__ == '__main__':
    # data for testing
    a = "Olivia simping for tylerz"
    b = "Drywall is drywall"
    c = "Hello drywall"

    # ascii testing
    a_ascii = convert_to_ascii(a)
    b_ascii = convert_to_ascii(b)
    c_ascii = convert_to_ascii(c)

    # ascii shift
    a_cipher_shift = cipher_shift(25,a_ascii)
    b_cipher_shift = cipher_shift(25,b_ascii)
    c_cipher_shift = cipher_shift(25,c_ascii)

    # dictionary creation and printing
    a_cipher_dict = frequency_analysis(a_cipher_shift)
    b_cipher_dict = frequency_analysis(b_cipher_shift)
    c_cipher_dict = frequency_analysis(c_cipher_shift)

    # TODO:
    # use llambda functions to display from highest to lowest value value's
    # print("A Message Frequency Analysis")
    # display_dict(a_cipher_dict)
    # print("B Message Frequency Analysis")
    # display_dict(b_cipher_dict)
    # print("C Message Frequency Analysis")
    # display_dict(c_cipher_dict)

    # print results
    # print("Input data: {}\nAscii: {}\nAscii Shift: {}\nOutput data: {}\n\n".format(display_cipher_shift(a_ascii),a_ascii,a_cipher_shift, display_cipher_shift(a_cipher_shift)))
    # print("Input data: {}\nAscii: {}\nAscii Shift: {}\nOutput data: {}\n\n".format(display_cipher_shift(b_ascii),b_ascii,b_cipher_shift, display_cipher_shift(b_cipher_shift)))
    # print("Input data: {}\nAscii: {}\nAscii Shift: {}\nOutput data: {}\n\n".format(display_cipher_shift(c_ascii),c_ascii,c_cipher_shift, display_cipher_shift(c_cipher_shift)))

    # test v cipher - test with key = 3
    print(v_cipher(3, a))


    print(len(convert_to_ascii(a)))
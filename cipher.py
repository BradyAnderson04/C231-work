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
    shift_value = n%26

    output_ascii = [0] * len(ascii_list)

    for i in range(len(ascii_list)):
        output_ascii[i] = ascii_list[i] + shift_value

        #TODO:
        # change logic to work with negative values too
        # also verify z maps properly 
        if(output_ascii[i] > 90):
            # when greater than 90 subtract 26 - 
            output_ascii[i] -= 26
    
    return output_ascii

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

    # print results
    print("Input data: {}\nAscii: {}\nAscii Shift: {}\nOutput data: {}\n\n".format(a,a_ascii,a_cipher_shift, display_cipher_shift(a_cipher_shift)))
    print("Input data: {}\nAscii: {}\nAscii Shift: {}\nOutput data: {}\n\n".format(b,b_ascii,b_cipher_shift, display_cipher_shift(b_cipher_shift)))
    print("Input data: {}\nAscii: {}\nAscii Shift: {}\nOutput data: {}\n\n".format(c,c_ascii,c_cipher_shift, display_cipher_shift(c_cipher_shift)))

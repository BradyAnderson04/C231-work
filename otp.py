'''code to do the otp operation'''

import random as rn

def create_bit_string(m):
    '''
    create a string to it's ascii binary equivalent

    m - the message to be converted
    '''
    output = " "
    output += ' '.join(format(ord(i), 'b') for i in m)
    return output.replace(" ", "0")

def generator(n):
    key = ""

    for i in range(n):
        key += str(rn.randint(0, 1))
    
    return key

def XORGate(x, y):
    if x != y:
        return 1
    else:
        return 0

def encrypt(key, m):
    '''
    function that perform xor encryption
    key - the key generated from generator function
    m - the message being encrypted
    '''
    encrypted_message = ""

    for i in range(len(m)):
        encrypted_message += str(XORGate(key[i], m[i]))

    return encrypted_message


if __name__ == "__main__":
    # data
    a = "MAKE PEACE"
    b = "DON'T MEOW"
    c = "MEXICO"
    d = "HISTORY"

    """
    Part a - find length of key 

    for otp the length of the key is the length of the message in bits

    a character has 8 bits associated with it so....

    use the definitions assigned above to the strings

    a = 8 * 10 = 80
    b = 8 * 10 = 80
    c = 8 * 6 = 48
    d = 8 * 7 = 56

    in general length of key = 8 * len(m)

    """
    

    # bit strings
    a_bit = create_bit_string(a)
    # print(a_bit)
    b_bit = create_bit_string(b)
    # print(b_bit)
    c_bit = create_bit_string(c)
    # print(c_bit)
    d_bit = create_bit_string(d)
    # print(len(d_bit))

    # key generators - part b
    a_key = generator(80)
    b_key = generator(80)
    c_key = generator(48)
    d_key = generator(56)
    # print(len(d_key))

    # encrypting - part c
    enc_a = encrypt(a_key, a_bit)
    enc_b = encrypt(b_key, b_bit)
    enc_c = encrypt(c_key, c_bit)
    enc_d = encrypt(d_key, d_bit)
    # print(len(enc_d))

    # display results
    print("Bit String: {:>}\nKey Bit: {:>}\nEncrypted Xor: {:>}\n".format(a_bit, a_key, enc_a))
    print("Bit String: {:>}\nKey Bit: {:>}\nEncrypted Xor: {:>}\n".format(b_bit, b_key, enc_b))
    print("Bit String: {:>}\nKey Bit: {:>}\nEncrypted Xor: {:>}\n".format(c_bit, c_key, enc_c))
    print("Bit String: {:>}\nKey Bit: {:>}\nEncrypted Xor: {:>}\n".format(d_bit, d_key, enc_d))




'''code to do the otp operation'''

import random as rn

class OTPEncryptor():
    # class attributes
    message=""
    message_length=0
    key=""

    def __init__(self,message):
        self.message=message
        self.message_length=len(message)
        self.key=self.generator(self.message_length)

    def create_bit_string(self, m):
        '''
        create a string to it's ascii binary equivalent

        m - the message to be converted
        '''
        output = " "
        output += ' '.join(format(ord(i), 'b') for i in m)
        return output.replace(" ", "0")

    def generator(self,n):
        """
        The generator function create a key randomly of length n

        n - length of the key
        """
        key = ""

        for i in range(n):
            key += str(rn.randint(0, 1))
        
        return key

    def XORGate(self,x,y):
        if x != y:
            return 1
        else:
            return 0

    def encrypt(self,key,m):
        '''
        function that perform xor encryption
        key - the key generated from generator function
        m - the message being encrypted
        '''
        # encrypted_message = ""

        # for i in range(len(m)):
        #     encrypted_message += str(XORGate(key[i], m[i]))

        return "".join([str(XORGate(key[i], m[i])) for i in range(len(m))])    

    def decrypt(self,key,encoded_m):
        '''
        function that perform xor decryption -- this is the exact same as encryption method just in different function for semantics sake
        key - the key generated from generator function
        encoded_m - the message being decrypted
        '''
        decrypted_message = ""

        # loop
        for i in range(len(encoded_m)):
            decrypted_message += str(XORGate(key[i], encoded_m[i]))

        return decrypted_message

if __name__ == "__main__":
    # data -- need to chane tester code to work with class based implementation
    a = "MAKE PEACE"
    b = "DON'T MEOW"
    c = "your not a trash cant you a trash CAN"
    d = "I am become meme, Destroyer of shorts"

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
    b_bit = create_bit_string(b)
    c_bit = create_bit_string(c)
    d_bit = create_bit_string(d)

    # key generators - part b
    a_key = generator(8*len(a)) # generate key length of 8 * length of string
    b_key = generator(8*len(b))
    c_key = generator(8*len(c))
    d_key = generator(8*len(d))

    # encrypting - part c
    enc_a = encrypt(a_key, a_bit)
    enc_b = encrypt(b_key, b_bit)
    enc_c = encrypt(c_key, c_bit)
    enc_d = encrypt(d_key, d_bit)
    
    # decrypting - part extra
    dec_a = decrypt(a_key, enc_a)
    dec_b = decrypt(b_key, enc_b)  
    dec_c = decrypt(c_key, enc_c) 
    dec_d = decrypt(d_key, enc_d) 

    # display results
    print("{}\n\nBit String: {:>}\nKey Bit: {:>}\nEncrypted Xor: {:>}\nDecrypted Xor: {:>}\n\nSuccessful Decryption ? {:>}\n\n\n".format(a,a_bit,a_key,enc_a,dec_a,a_bit==dec_a))
    print("{}\n\nBit String: {:>}\nKey Bit: {:>}\nEncrypted Xor: {:>}\nDecrypted Xor: {:>}\n\nSuccessful Decryption ? {:>}\n\n\n".format(b,b_bit,b_key,enc_b,dec_b,b_bit==dec_b))
    print("{}\n\nBit String: {:>}\nKey Bit: {:>}\nEncrypted Xor: {:>}\nDecrypted Xor: {:>}\n\nSuccessful Decryption ? {:>}\n\n\n".format(c,c_bit,c_key,enc_c,dec_c,c_bit==dec_c))
    print("{}\n\nBit String: {:>}\nKey Bit: {:>}\nEncrypted Xor: {:>}\nDecrypted Xor: {:>}\n\nSuccessful Decryption ? {:>}\n\n\n".format(d,d_bit,d_key,enc_d,dec_d,d_bit==dec_d))

    # display what XOR means
    print("XOR Logic:\n0 0 | {}\n0 1 | {}\n1 0 | {}\n1 1 | {}\n".format(XORGate(0,0), XORGate(0,1), XORGate(1,0), XORGate(1,1)))

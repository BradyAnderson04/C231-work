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

# create a class

class CeasarCipher():

    def __init__(self, shift):
        pass

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
        # process won't work due to the order of key gens -- so I'll just call these in the order I need in function -- depreciated
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
            if(freq_dict.get(chr(val)) is not None):
                freq_dict[chr(val)] += 1 # increment value
            else:
                freq_dict[chr(val)] = 1 # create and init value

        return freq_dict

    def display_dict(freq_dict):
        # iterate over keys and print the key value pair
        for key in sorted(freq_dict):
            print(key,":",freq_dict[key])


class VCipher(ceasar_cipher):
        
        __init__(self, key_size):
            pass
        
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
        m = convert_to_ascii(message)
        loop_count = math.ceil(len(m) / key_size)

        output = [] # message encoded
        shift_outputs = [] # list of shift values
        
        for i in range(loop_count):
            # genearte a shift value
            temp_shift = rn.randint(0, 26) # generate val from 0 - 26 inc.
            # perform cipher shift on substring

            # define message substring to use
            bound_s = (i) * key_size
            bound_e = (i+1) * key_size
            m_sub = m[bound_s: bound_e]

            output_ascii = cipher_shift(temp_shift, m_sub) # generate ascii of length key_size
            
            # save to output
            shift_outputs.append(temp_shift)
            [output.append(x) for x in output_ascii]
        
        # return output
        return output, shift_outputs


if __name__ == '__main__':
    # data for testing
    a = "Olivia reading for tyler"
    b = "Drywall is drywall"
    c = "Hello drywall"

    # # ascii testing
    # a_ascii = convert_to_ascii(a)
    # b_ascii = convert_to_ascii(b)
    # c_ascii = convert_to_ascii(c)

    # ascii shift
    # a_cipher_shift = cipher_shift(25,a_ascii)
    # b_cipher_shift = cipher_shift(25,b_ascii)
    # c_cipher_shift = cipher_shift(25,c_ascii)

    # dictionary creation and printing
    # a_cipher_dict = frequency_analysis(a_cipher_shift)
    # b_cipher_dict = frequency_analysis(b_cipher_shift)
    # c_cipher_dict = frequency_analysis(c_cipher_shift)

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
    


    # print("Output:", display_cipher_shift(result[0]))
    # print("Keys_size: 3")
    # print("Shift Values:", result[1])

    print("For all parts of Q7, I made use of python 3.8 and visual studio code to generate the code along with github to host and share what the code is with the TA/UI staff for C231.")

    # problem 7 - setup
    dream_speech = "I am not unmindful that some of you have come here out of great trials andtribulations.  Some of you have come fresh from narrow jail cells.  Some of youhave come from areas where your quest for freedom left you battered by thestorms of persecution and staggered by the winds of police brutality.You have been the veterans of creative suffering.Continue to work with the faith that unearned suffering is redemptive.Go back to Mississippi.  Go back to Alabama.  Go back to South Carolina.  Goback to Georgia.  Go back to Louisiana.  Go back to the slums and ghettosof our Northern cities, knowing that somehow this situation can and will bechanged.  Let us not wallow in the valley of despair.I say to you today, my friends, so even though we face the difficulties of todayand tomorrow, I still have a dream.It is a dream deeply rooted in the American dream.I  have  a  dream  that  one  day  this  nation  will  rise  up  and  live  out  the  truemeaning of its creed, “We hold these truths to be self-evident, that all menare created equal.”I have a dream that one day on the red hills of Georgia, sons of former slavesand the sons of former slave owners will be able to sit down together at thetable of brotherhood.I have a dream that one day even the state of Mississippi, a state swelteringwith  the  heat  of  injustice,  sweltering  with  the  heat  of  oppression,  will  betransformed into an oasis of freedom and justice.I have a dream that my four little children will one day live in a nation wherethey will not be judged by the color of their skin but by the content of theircharacter.I have a dream today!"

    ascii_data = convert_to_ascii(dream_speech)
    
    

    # part a - ceasar Cipher
    even_or_odd = rn.randint(1, 2)
    multiplyer = math.pow(-1, even_or_odd)
    random_shift = int(rn.randint(0, 25) * multiplyer)

    ceazar = cipher_shift(random_shift, ascii_data)

    # print("Q7 Part A\n" + "_"*100)
    # print("Ceazar Cipher:", display_cipher_shift(ceazar))
    # print("Shift Values:", random_shift)
    
    # # part b - vigenere cipher:
    # random_key = int(rn.randint(0, 5))

    # vignenere = v_cipher(random_key, dream_speech)


    # print("\nQ7 Part B\n" + "_"*100)
    # print("Output:", display_cipher_shift(vignenere[0]))
    # print("Keys_size:", random_key)
    # print("Shift Values:", vignenere[1])

    # part c - frequency count for both -- ordering keys from
    # print("\nQ7 Part C\n" + "_"*100)
    # c_freq_analysis = frequency_analysis(ceazar)
    # v_freq_analysis = frequency_analysis(vignenere[0])

    # print("The frequency analysis of ceazar cipher shift -- notice the higher concentration of values")
    # display_dict(c_freq_analysis)

    # print("The frequency analysis of vigenere shift -- notice the lower concentration of values")
    # display_dict(v_freq_analysis)

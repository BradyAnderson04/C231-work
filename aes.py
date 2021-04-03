'''
A file for the NIST definition of AES 2001


Parr - confusion and diffusion 

stallings - structure
'''

# Hexadecimal to binary conversion 
def hex2bin(s): 
    mp = {'0' : "0000",  
          '1' : "0001", 
          '2' : "0010",  
          '3' : "0011", 
          '4' : "0100", 
          '5' : "0101",  
          '6' : "0110", 
          '7' : "0111",  
          '8' : "1000", 
          '9' : "1001",  
          'A' : "1010", 
          'B' : "1011",  
          'C' : "1100", 
          'D' : "1101",  
          'E' : "1110", 
          'F' : "1111" } 
    bin = ""
    for i in s:
        bin += mp[i]
    return bin
 
# Binary to hexadecimal conversion 
def bin2hex(s): 
    mp = {"0000" : '0',  
          "0001" : '1', 
          "0010" : '2',  
          "0011" : '3', 
          "0100" : '4', 
          "0101" : '5',  
          "0110" : '6', 
          "0111" : '7',  
          "1000" : '8', 
          "1001" : '9',  
          "1010" : 'A', 
          "1011" : 'B',  
          "1100" : 'C', 
          "1101" : 'D',  
          "1110" : 'E', 
          "1111" : 'F' } 
    hex = "" 
    for i in range(0,len(s),4): 
        ch = "" 
        ch = ch + s[i] 
        ch = ch + s[i + 1]  
        ch = ch + s[i + 2]  
        ch = ch + s[i + 3]  
        hex = hex + mp[ch] 
          
    return hex
  
# Binary to decimal conversion 
def bin2dec(binary):  
    binary1 = binary  
    decimal, i, n = 0, 0, 0
    while(binary != 0):  
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)  
        binary = binary//10
        i += 1
    return decimal 
  
# Decimal to binary conversion 
def dec2bin(num):  
    res = bin(num).replace("0b", "") 
    if(len(res)%4 != 0): 
        div = len(res) / 4
        div = int(div) 
        counter =(4 * (div + 1)) - len(res)  
        for i in range(0, counter): 
            res = '0' + res 
    return res 

def leftShift(binary):
    # left shift
    s = binary[8:] + binary[:8]
    # convert to hex
    return bin2hex(s)

def xor(a, b): 
    ans = ""
    for i in range(len(a)): 
        if a[-i] == b[-i]: 
            ans = ans + "0"
        else: 
            ans = ans + "1"
    if(len(b) > len(a)):
        return b[len(a):] + ans
    return ans

def mixcol(a, b):
    '''
    This doesn't include the modular operation so the output is in binary values so can do the multiplication

    kinda sucks gonna have to do mod operation
    a - the message in question
    b - the static matrix
    '''
    output = [[]]
    output2 = [[]]
    for k in range(len(a)):
        for i in range(len(a)):
            # iterate over every row
            tempsum = '000000000'
            for j in range(len(a[0])):
                # iterate over every column
                
                # dynamically increase size of list
                if(i < len(output)):
                    output.append([])
                    output2.append([])
                # sum the resulting value for i j index
                print(a[k][j])
                if(b[j][i] == 1):
                    tempsum = xor(str(bin(int(hex2bin(a[k][j]), 2))), tempsum)
                elif(b[j][i] == 2):
                    # left shift each bit by 1 
                    tempsum = xor(str(bin(int(hex2bin(a[k][j]), 2)<<1))[2:], tempsum)
                else:
                    # left shift input xor input
                    tempsum = xor(xor(str(bin(int(hex2bin(a[k][j]), 2)<<1))[2:], tempsum), xor(str(bin(int(hex2bin(a[k][j]), 2))), tempsum))

            # do the modular arithmatic
            p = '100011011'
            
            # leaving the inner for loop add this temp sum to output result
            output[k].append(xor(tempsum, str(bin(int(p, 2)<<(len(a) - len(b))))[2:] ))
            output2[k].append(tempsum)
    print(f'the output of the mod multiplication is \n{output[0]}\n{output[1]}\n{output[2]}\n{output[3]}')
    return output2

if __name__ == '__main__':
    # mixcol data setup
    w0 = "2B7E1516"
    w1 = "28AED2A6"
    w2 = "ABF71588"
    w3 = "09CF4F3C"
    
    print(f"w0 is {hex2bin(w0)}")
    print(f"w1 is {hex2bin(w1)}")
    print(f"w2 is {hex2bin(w2)}")
    print(f"w3 is {hex2bin(w3)}")

    print(f"left shift of w3 is {leftShift(hex2bin(w3))}")

    gw3 = xor(hex2bin('8A84EB01'), hex2bin('01000000'))
    print(f"g(w3) is {gw3}")

    w4 = xor(gw3, hex2bin(w0))
    w5 = xor(w4, hex2bin(w1))
    w6 = xor(w5, hex2bin(w2))
    w7 = xor(w6, hex2bin(w3))

    print(f"w4 = {gw3} xor {hex2bin(w0)} = {w4}")
    print(f"w4 = {w4} xor {hex2bin(w1)} = {w5}")
    print(f"w4 = {w5} xor {hex2bin(w2)} = {w6}")
    print(f"w4 = {w6} xor {hex2bin(w3)} = {w7}")

    print(f'w4 final result is {w4} w/ len {len(w4)}, hex is {bin2hex(w4)}')
    print(f'w5 final result is {w5} w/ len {len(w5)}, hex is {bin2hex(w5)}')
    print(f'w6 final result is {w6} w/ len {len(w6)}, hex is {bin2hex(w6)}')
    print(f'w7 final result is {w7} w/ len {len(w7)}, hex is {bin2hex(w7)}\n\n\n\n')

    a = [['F1', 'F2', '59', '47'],
         ['24', '34', 'E4', 'B5'],
         ['59', 'C4', '62', '68'],
         ['8A', '84', 'EB', '01']]

    b = [[2, 3, 1, 1],
         [1, 2, 3, 1],
         [1, 1, 2, 3],
         [3, 1, 1, 2]]

    result = mixcol(a, b)
    print(f'the output of the mod multiplication is \n{result[0]}\n{result[1]}\n{result[2]}\n{result[3]}')

    p = '1000110110'
    pbase = '100011011'
    print(xor(p, '1000110000'))
    print(xor(p, '1101000101'))
    print(xor(pbase, '110110011'))
    print(xor(p, '1111010100'))

    print()

    print(xor(p, '1011110001'))
    print(xor(p, '1011101111'))
    print(xor(p, '1000110000'))

    print()

    print(xor(pbase, '110100010'))
    print(xor(p, '111011001'))
    print(xor(p, '1011100111'))
    print(xor(pbase, '101001110'))

    print()

    print(xor(p, '1100101001'))

    message = "11000000100111010001010110001111110001100011011011000000010110001001110111101111000101101010101000010000111011011111000101110101"
    print(len(message))

    print(xor(message, w4+w5+w6+w7))

    print(bin2hex("01000001001000101110010110011111010110001111001101010001001000001001101001111111101100001111110000010011110000011101100101111111"))



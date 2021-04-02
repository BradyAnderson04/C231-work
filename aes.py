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
    print(len(binary[:8]))
    s = binary[8:] + binary[:8]
    # convert to hex
    return bin2hex(s)

def xor(a, b): 
    ans = "" 
    for i in range(len(a)): 
        if a[i] == b[i]: 
            ans = ans + "0"
        else: 
            ans = ans + "1"
    return ans 

if __name__ == '__main__':
    w0 = "2B7E1516"
    w1 = "28AED2A6"
    w2 = "ABF71588"
    w3 = "09CF4F3C"
    
    print(f"w0 is {hex2bin(w0)}")
    print(f"w1 is {hex2bin(w1)}")
    print(f"w2 is {hex2bin(w2)}")
    print(f"w3 is {hex2bin(w3)}")

    print(f"left shift of w3 is {leftShift(hex2bin(w3))}")

    print(f"g(w3) is {hex2bin('8A84EB01')}")

    w4 = xor('10001010100001001110101100000001', '00101011011111100001010100010110')
    w5 = xor(w4, hex2bin(w1))
    w6 = xor(w5, hex2bin(w2))
    w7 = xor(w6, hex2bin(w3))

    print(f'w4 final result is {w4} w/ len {len(w4)}')
    print(f'w5 final result is {w5} w/ len {len(w5)}')
    print(f'w6 final result is {w6} w/ len {len(w6)}')
    print(f'w7 final result is {w7} w/ len {len(w7)}')

'''
Author: Brady Anderson
Date: 3/19/2021
Description: 
A program that calculates some properties of galois fields

COMPLETE:
    priority:
        additive and multiplicative inverse

TODO:
    Non-priority Operations of fields:
    Addition operations:
        Closure
        associative
        commutative

    Multiplication operations:
        closure
        associative
        distributive
        commutative
        identity
        no zero divisors
'''

# code for assignment 6

import math

class Galois_Field():

    def __init__(self, p, m=1):
        # constructor of a Galois field object
        self.p = p
        self.m = m
        self.n = int(math.pow(self.p, self.m))
        self.elements = [i for i in range(self.n)]

    def to_string(self):
        print(self.elements)

    def calc_additive_inverse(self, x):
        '''
        given the p value find the additive inverse that satisfies the relationship

        there is an additive inverse when a + -a = 0 mod n
        '''
        # fix value to be in proper range
        x = x % self.n
        # base case
        if(x == 0):
            return 0
        else:
            # case where valid value
            return self.n - x 

    def calc_multiplicative_inverse(self, x):
        '''
        given the p value and x find the multiplicative inverse of x that satisfies the relationship
        for a galois prime field. This 

        1 = xs + nt

        x = 1-nt / x

        using t = 1 for simplicity sake
        '''
        # calc base condition
        gcd = self.gcd(x)

        if(gcd != 1):
            # there is no inverse value for this x and p when gcd != 1
            return None
        else:
            # inverse value exists, return the formula solution
            t = 1
            # find t value that divides evenly
            while((self.n * t + 1) % x != 0):
                t += 1
            # fml to calculate inverse
            return ((self.n * t  + 1) / x) % self.n

    def gcd(self, x):
        '''
        find the gcd between x and self.p

        gcd is the greatest integer that divides both numbers included
        '''
        # normalize value in the correct range
        x = x % self.n
        # edge case 
        if(x == 0):
            return 0
        # default value
        val = 0
        # iterate through to id the gcd
        for i in range(1, int(math.pow(self.p,self.m))):
            # check for remainder
            y, z = self.n%i, x%i
            if(y == 0 and z == 0):
                val = i
        
        return val

# some helper functions
def generate_field_elements(p, n):
    for l in range(p):
        for i in range(p):
            for j in range(p):
                for k in range(p):
                    print(f"{k}x^3+{j}x^2+{i}x+{l}")
                    # print(f"({l} {i} {j} {k})")

def xor(a, b): 
    ans = "" 
    for i in range(len(a)): 
        if a[i] == b[i]: 
            ans = ans + "0"
        else: 
            ans = ans + "1"
    return ans 


if __name__ == '__main__':
    # create a test object for problem 6
    test = Galois_Field(113)

    a = "11111111"
    b = "10000010"
    c = "00100000"
    d = "00000000"

    print(xor(xor(b, c), d))
    print(xor(xor(a, c), d))
    print(xor(xor(a, b), d))
    print(xor(xor(a, b), c))

    # testing multiplicative inverse of galois field
    # print("Multiplicative Inverse:")
    # for i in range(1, test.n):
    #     temp = test.calc_multiplicative_inverse(i)
    #     print(f"Input: {i}, Multiplicative Inverse:{temp} Result: {i} * {temp} % {test.n} = {(i * temp) % test.n} mod {test.n}")

    # testing additive inverse of galois field
    # print("\n\nAdditive Inverse:")
    # for j in range(0, test.n):
    #     temp = test.calc_additive_inverse(j)
    #     print(f"Input: {j}, Additive Inverse: {temp} Result: {j} + {temp} = {(j + temp) % test.n} mod {test.n}")

    # generate_field_elements(2, 4)
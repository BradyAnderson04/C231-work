'''
Author: Brady Anderson
Date: 3/19/2021
Description: 
A program that calculates some properties of galois fields

priority:
additive and multiplicative inverse

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
import math

class Galois_Field():

    def __init__(self, p, m=1):
        self.p = p
        self.m = m
        self.n = int(math.pow(self.p, self.m))
        self.elements = [i for i in range(self.n)]

    def to_string(self):
        print(self.elements)

    def calc_additive_inverse(self):
        '''
        given the p value find the additive inverse that satisfies the relationship


        '''
        pass

    def calc_multiplicative_inverse(self, x):
        '''
        given the p value and x find the multiplicative inverse of x that satisfies the relationship
        for a galois prime field. This 

        1 = xs + nt

        x = 1-nt / x

        using t = 1 for simplicity sake
        '''
        gcd = self.gcd(x)

        if(gcd != 1):
            # there is no inverse value for this x and p
            return None
        else:
            # inverse value exists, return the formula solution
            t = 1
            # find t value
            while((self.n * t + 1) % x != 0):
                t += 1
            return ((self.n * t  + 1) / x) % self.n

    def gcd(self, x):
        '''
        find the gcd between x and self.p

        gcd is the greatest integer that divides both numbers included
        '''
        x = x % self.n
        if(x == 0):
            return 0
        val = 0
        for i in range(1, int(math.pow(self.p,self.m))):
            y, z = self.n%i, x%i
            if(y == 0 and z == 0):
                val = i
        
        return val

    

if __name__ == '__main__':
    test = Galois_Field(8)

    print(test.gcd(0))

    print(f"Input: 0, Multiplicative Inverse: {test.calc_multiplicative_inverse(0)}")
    print(f"Input: 1, Multiplicative Inverse: {test.calc_multiplicative_inverse(1)}")
    print(f"Input: 2, Multiplicative Inverse: {test.calc_multiplicative_inverse(2)}")
    print(f"Input: 3, Multiplicative Inverse: {test.calc_multiplicative_inverse(3)}")
    print(f"Input: 4, Multiplicative Inverse: {test.calc_multiplicative_inverse(4)}")
    print(f"Input: 5, Multiplicative Inverse: {test.calc_multiplicative_inverse(5)}")
    print(f"Input: 6, Multiplicative Inverse: {test.calc_multiplicative_inverse(6)}")
    print(f"Input: 7, Multiplicative Inverse: {test.calc_multiplicative_inverse(7)}")

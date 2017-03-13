# -*- coding: utf-8 -*-
def gcdRecur(a,b):
    '''
    a, b: positive integer
    
    returns: a positive integer, the greatest common divisor of a & b/
    '''
    if b == 0:
        return a
    return gcdRecur(b, a%b)

    
print(gcdRecur(2,12))
print(gcdRecur(6,12))
print(gcdRecur(9,12))
print(gcdRecur(17,12))

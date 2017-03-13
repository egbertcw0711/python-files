# -*- coding: utf-8 -*-
def gcdIter(a,b):
    '''
    a,b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    i = a
    while i > 1:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1
    return 1
    
print(gcdIter(2,12))
print(gcdIter(6,12))
print(gcdIter(9,12))
print(gcdIter(17,12))


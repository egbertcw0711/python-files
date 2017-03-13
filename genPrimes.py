# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:10:08 2017

@author: egbertcw
"""

def genPrimes():
    p = []
    x = 2
    yield x
    p.append(x)
    while True:
        x += 1
        for e in p:
            if(x % e == 0):
                break
        else:
            p.append(x)
            yield x  
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 19:43:30 2017

@author: egbertcw
"""

def f(y):
    x = 1
    def h():
        x = 'abc'
    print('In f x = ', x)
    #x = x + 1
    #return x
    
x = 3
z = f(x)
print('In Global x = ', x)
print('z = ', z)
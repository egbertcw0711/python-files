# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 19:20:24 2017

@author: egbertcw
"""
def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item / denom  
    except:
        return 0
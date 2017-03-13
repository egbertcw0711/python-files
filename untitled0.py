# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 19:51:58 2017

@author: egbertcw
"""
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    length_L = len(L)
    assert length_L >= 2, 'invalid input list'
    tmp_in = []
    tmp_de = []
    incr = []
    decr = []
    cur_inidx = 0
    cur_deidx = 0
    for i in range(length_L-1):
        if(L[i] <= L[i+1]):
            tmp_in.append(L[i])
            if(i == length_L-2):
                tmp_in.append(L[i+1])
                if(len(tmp_in) > len(incr)):
                    incr = tmp_in          #special case: reaches end of the list
                    cur_inidx = i+1
        else:
            tmp_in.append(L[i])   
            if(len(tmp_in) > len(incr)):
                incr = tmp_in
                cur_inidx = i
            tmp_in = []

    for j in range(length_L-1):
        if(L[j] >= L[j+1]):
            tmp_de.append(L[j])
            if(j == length_L-2):
                tmp_de.append(L[j+1])
                if(len(tmp_de) > len(decr)):
                    decr = tmp_de[:]
                    cur_deidx = j+1
        else:
            tmp_de.append(L[j])
            if(len(tmp_de) > len(decr)):
                decr = tmp_de[:]
                cur_deidx = j
            tmp_de = []

    if(len(incr) > len(decr)): return sum(incr)
    elif(len(incr) < len(decr)): return sum(decr)
    else:
        if(cur_inidx < cur_deidx): return sum(incr)
        else:return sum(decr)
    
            



    
    
trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

          
def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    if(int(us_num) <= 10 and int(us_num) >= 0 ):
        return trans[us_num]
    elif(int(us_num) > 10 and int(us_num) < 20):
        return trans['10']+' '+trans[str(int(us_num)%10)]
    else:
        if(int(us_num)%10 != 0):
            return trans[str(int(us_num)//10)]+' '+trans['10']+' '+trans[str(int(us_num)%10)]
        else:
            return trans[str(int(us_num)//10)]+' '+trans['10']
        
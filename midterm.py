# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 09:17:13 2017

@author: egbertcw

"""
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    lst = []
    for i in aList:
        if type(i) != list:
            lst.append(i)
        else:
            lst = lst + flatten(i)
    return lst
    #return aList

#def f(i):
#    return i + 2
    
#def g(i):
 #   return i > 5

#def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
#    Lnew = L[:]
#    for i in Lnew:
#        if not g(f(i)):
#            L.remove(i)
            
#    if len(L) == 0:
 #       return -1
  #  return max(L)
    
    
    
    
    
#def f(a,b):
#    return a>b

#def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
#    te = ()
#    dic1 = {}
#    dic2 = {}
#    for key1,value1 in d1.items():
 #           if (key1 in d2):
 #               dic1[key1] = f(value1, d2[key1])
 ##           else:
 #               dic2[key1] = value1
#
  #  for key2, value2 in d2.items():
  #      if(key2 not in d1):
#            dic2[key2] = value2 
  #  te = (dic1,dic2)
    
  #  return te
        
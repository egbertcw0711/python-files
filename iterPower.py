# -*- coding: utf-8 -*-
def iterPower(base, exp):
    '''
    base: int or float
    exp: int >= 0
    returns: int or float base ^ exp
    '''
    ans = 1.0
    if exp == 0:
        return ans
    else:
        for i in range(exp):
            ans = base * ans
        return ans
    
print(iterPower(-9.49,0))


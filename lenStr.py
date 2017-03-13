# -*- coding: utf-8 -*-
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetical string
    
    returns: True if char is in aStr; Flase otherwise
    '''
    lenStr = len(aStr)
    if lenStr == 0:
        return False
    elif lenStr == 1:
        if char == aStr:
            return True
        else:
            return False
    else:
        lenStr = lenStr // 2
        if char == aStr[lenStr]:
            return True;
        else:
            if char < aStr[lenStr]:
                aStr = aStr[:lenStr]
                return isIn(char, aStr)
            else:
                aStr = aStr[lenStr + 1:]
                return isIn(char, aStr)

print(isIn('a', 'a'))
print(isIn('a', ''))
print(isIn('a', 'b'))
print(isIn('a', 'assdas'))

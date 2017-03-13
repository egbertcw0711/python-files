# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 08:08:09 2017

@author: egbertcw
"""

import math

def polysum(n,s):
    area = 0.25 * n * s * s / (math.tan(math.pi / n))
    perimeter = n * s
    return round(area + perimeter*perimeter,4)
    
print(polysum(48,26))
print(polysum(4,2))
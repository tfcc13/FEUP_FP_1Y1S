#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:42:06 2022

@author: tiago
"""

import math

def factorial(i,j):
    value = math.factorial(i)/math.factorial(j)/math.factorial(i-j)
    return int(value)
    
def pascal(n):
    result = ""
    
    for i in range(n):
        for j in range(i+1):
            if j > 0:
                result = result + " " + str(factorial(i,j))
            else:
              result = result + "" + str(factorial(i,j))
        result = result + "\n"
    
    return result
    
print(pascal(3))


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:42:21 2022

@author: tiago
"""

import math


def digits_average(n):
    avg = 0
import math

def digits_average(n):
    avg = 0
    if abs(n) < 10:
        return n 
    while abs(n) > 10:
        n1 = n % 10
        n2 = n // 10 % 10
        avg = math.ceil((avg + (n2+n1)/2)/2)
        n = n// 10
    return avg
        
        
    
print(digits_average(-12))
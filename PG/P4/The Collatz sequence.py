#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:51:31 2022

@author: tiago
"""

def collatz(n):
    result = str(n)
    
    while n != 1:
        if n%2  == 0:
            n = int(n / 2)
        else:
            n = int(n*3 + 1)
        result = result + "," + str(n)
    return result

print(collatz(10))
    
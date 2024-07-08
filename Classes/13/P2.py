#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 10:16:38 2022

@author: tiago
"""

def find_me(f, limits):
    iters = 0
    upper = limits[1]
    lower = limits[0]
    
    while True:
        iters +=1
        n = (upper+lower) // 2
        if f(n) == 1:
            lower = n+1
        elif f(n) == -1:
            upper = n-1

        else:
            return iters
    
    
        
print(find_me(lambda n: -1 if n > 30 else 1 if n < 30 else 0, (0, 100)))
print(find_me(lambda n: -1 if n > -891 else 1 if n < -891 else 0, (-1000, 10000)))
print(find_me(lambda n: -1 if n > 563 else 1 if n < 563 else 0, (-5000, 5000)))
print(find_me(lambda n: 0 if n == 99 else 1, (0, 100)))
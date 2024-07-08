#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:09:27 2022

@author: tiago
"""

def comprehensions(i,j):
    
    x = [x for x in range(i,j+1) if (x % 10 == 3 or x % 10 == 8)]
    t = tuple(round((t)**0.5,2) for t in range(i,j+1))
    z = {z:chr(z) for z in range(i,j+1)}
    
    return x,t,z
    
print(comprehensions(100, 102))
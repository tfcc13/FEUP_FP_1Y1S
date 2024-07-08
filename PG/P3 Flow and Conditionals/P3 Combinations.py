#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 18:09:04 2022

@author: tiago
"""

def c(n,r):
    k = n-r
    factorial_n = 1
    factorial_r = 1
    factorial_k = 1
    
    for i in range(1,n+1):
        factorial_n = factorial_n * i
    for i in range(1,r+1):
        factorial_r = factorial_r * i
    for i in range(1,k+1):
        factorial_k = factorial_k * i
    
    c = factorial_n / (factorial_k * factorial_r)

    return int(c)


print(c(9,3))
        
        
            
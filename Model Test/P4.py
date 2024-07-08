#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 14:18:21 2022

@author: tiago
"""

def is_prime(n):
    count = 0
    for i in range(2, n+1):
        if n % i == 0:
            count += 1
    return count == 1

def primes_difference(n):
    
    while True:
        if is_prime(n) == True:
            smaller = n
            break
        else:
            n = n-1
    
    while True:
        if is_prime(n+1) == True:
            bigger = n+1
            break
        else:
            n = n+1
            
    print(bigger)
    print(smaller)
        
    return bigger-smaller
            
        
        
    
    
print(primes_difference(193))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:23:53 2023

@author: tiago
"""

def get_composites(n):
   
    numbers = [x for x in range(4,n+1)]
    primes = [y for y in numbers if all(y%z != 0 for z in range(2,y))]
    comp = list(filter(lambda c: c not in primes, numbers))
    
    
    for k in comp:
        yield k
    
   
def get_composites(n):
    return filter(lambda x: not all(map(lambda y: x % y != 0, range(2, x))), range(4, n+1))

print(list(get_composites(5)))
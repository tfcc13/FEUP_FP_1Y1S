#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:52:03 2022

@author: tiago
"""

def is_pair_of_square(m1,m2):
    count = 1
    new = 0 
    square = m2*m2
    size = len(str(m1))
    newsquare = 0
    mt = m1
    while mt > 0:
        
        new += mt % 10 * 10 ** (size-count)
        mt = mt // 10
        count += 1
    
    count1 = 1
    
    sizesq = len(str(square))
    while square > 0:
        newsquare += square % 10 * 10**(sizesq-count1)
        square = square // 10
        count1 += 1
    
    
    print(newsquare)
    print(new)
    print(m1)
    print(m1*m1)
        
    
    if new != m2 or newsquare != m1*m1 or m1==m2:
        return False
    return True
    
print(is_pair_of_square(111, 111))
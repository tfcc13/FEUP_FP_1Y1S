#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 13:01:01 2022

@author: tiago
"""

def greatest_member(a_tuple):

    result = a_tuple[0]
    points = 0
    
    
    for i in a_tuple:
        if some_points(i) > points:
            points = some_points(i)
            result = i
        
    return result
            
def some_points(tup):
    atup = ()
    
    
    if type(tup) != str:
        for k in tup:
            atup += (some_points(k),)
            points = sum(atup)
    else:
        for k in tup:
            atup += (ord(k),)
            points = sum(atup)
    return points
    
    
                
print(greatest_member(('abc', 'def', 'jkl', ('abc', 'def', ('123', 'jkl')))))
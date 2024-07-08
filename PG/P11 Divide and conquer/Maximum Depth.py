#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:53:24 2023

@author: tiago
"""

def maximum_depth(l):
    
    if l == []:
        return 1
    
    maximum = 0
    
    for i in l:
        if maximum_depth(i) > maximum:
            maximum = maximum_depth(i)
    return maximum + 1
    
    
print(maximum_depth([[], [[]], [], [[]]]))

def maximum_depth(l):
    if len(l) == 0:
        return 1
    else:
        return  1 + max(map(maximum_depth, l)) 
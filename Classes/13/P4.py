#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 19:20:05 2022

@author: tiago
"""

def bisect(f, n):
    lower = 0
    upper = 1
    
    for i in range(n):
        middle = (lower + upper) / 2
        if (f(lower) < 0 and f(middle) < 0) or (f(lower) > 0 and f(middle) > 0):
            lower = middle
        else:
            upper = middle
    return round(middle,5)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 12:29:14 2023

@author: tiago
"""

import math

def average(a, b):
    return math.ceil((a + b) / 2) 
def digits_average(n):
    m =0
    if n <10:
        return n
    else:
        def avg(n,m):
            if n<10:
                return m
            else:
                m =m*10 + average(n%10, (n//10)%10)
                return avg(n//10,m)
        m = avg(n,m)
        return digits_average(m)  
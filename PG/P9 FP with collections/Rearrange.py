#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 09:14:50 2023

@author: tiago
"""

def rearrange(l):
    x = list(filter(lambda j : j <= 0, l))
    y = list(filter(lambda k: k > 0, l))
    
    return x+y


print(rearrange([12, 11, -13, -5, 6, -7, 5, -3, -6, 0]))
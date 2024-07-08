#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:21:14 2023

@author: tiago
"""

def rearrange(l):
    return [j for j in l if j <= 0] + [k for k in l if k > 0]
    
    

def rearrange(l):
    return sorted(l, key = lambda x: (x>0,x<=0))

print(rearrange([12, 11, -13, -5, 6, -7, 5, -3, -6, 0]))
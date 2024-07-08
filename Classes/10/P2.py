#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 13:20:39 2022

@author: tiago
"""

def flatten(alist):
    if alist == []:
        return alist
    if type(alist[0]) == list:
        return  flatten(alist[0]) + flatten(alist[1:])
    else: 
        return alist[:1]+flatten((alist[1:]))
    
print(flatten(['Hello', [2, [[], False]], [True]]))
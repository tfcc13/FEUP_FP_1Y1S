#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 00:42:18 2022

@author: tiago
"""

def max_path(tree):
    if type(tree) is not tuple:
        return tree
    else:
        return tree[1] + max(max_path(tree[0]),(max_path(tree[2]))) 
    
print(max_path((1, 3, 2)))
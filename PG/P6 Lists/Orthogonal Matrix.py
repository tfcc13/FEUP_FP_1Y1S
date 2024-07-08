#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 16:15:32 2022

@author: tiago
"""

def is_orthogonal(mx):
    col = len(mx[0])

    t = []
        
    for i in range(col):
        l =[]
        for j in range(col):
            total = 0
            for k in range(col):
                total += mx[i][k] * mx[j][k]
            l.append(total)
        t.append(l)
            
    for i in range(col):
        for j in range(col):
            if i == j and t[i][j] != 1:
                return False
            if i != j and t[i][j] != 0:
                return False
    return True
        
            

print(is_orthogonal([[-1, 0], [0, 1]]))
print(is_orthogonal([[-2, 3], [4, -1]]))

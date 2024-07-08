#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 17:18:49 2022

@author: tiago
"""

def dict2list(adict,m,n):
    rows = []
    cols = []
    for i in adict.keys():
        if i[0] > m-1 or i[1] > n-1:
            return None
    for i in range(m):
        rows = []
        for k in range(n):
            x = adict.get((i,k),0)
            rows.append(x)
        cols.append(rows)
    return cols
            
    
print(dict2list({(0, 1): 4, (2, 1): 6}, 2, 3))
print(dict2list({(0, 1): 4, (1, 2): 6}, 2, 3))
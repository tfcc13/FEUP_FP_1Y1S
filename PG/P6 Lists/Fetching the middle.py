#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 16:35:21 2022

@author: tiago
"""

def fetch_middle(llists):
    
    result = []
    
    for i in llists:
        x = len(i)
        if x % 2 == 0:
            avg = (i[(x//2)-1]+i[x//2])/2

            result.append(avg)
        else:
            result.append(i[x//2])
    return(result)

print(fetch_middle([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]))
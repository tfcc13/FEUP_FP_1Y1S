#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 00:54:16 2022

@author: tiago
"""

def treasure(clues):
    y = clues.copy()
    if (0,0) not in clues.keys():
        return (0,0)
    for i in clues.items():
        if i[1] in y.keys():
            x = clues[i[1]]
            y.pop(i[1])
    return x

""" 
def treasure(clues):
    k = len(clues)
    i = res = 0
    aux = (0, 0)
    while i < k:
        res = aux
        aux = clues.get(res)
        i += 1
    
    return aux """
print(treasure({(0, 0): (1, 0), (2, 1): (3, 5), (1, 0): (2, 1)}))
print(treasure( {(0, 0): (1, 0), (1, 0): (2, 0), (2, 0): (3, 0)}))
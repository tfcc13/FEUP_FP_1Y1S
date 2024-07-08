#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 16:24:15 2022

@author: tiago
"""

def bagdiff(xs,ys):
    result =[]
    for i in ys:
        if i in xs:
            xs.remove(i)
               
    return xs
print(bagdiff([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]))
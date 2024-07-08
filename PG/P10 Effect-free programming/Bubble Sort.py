#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 14:54:21 2023

@author: tiago
"""

def bubble_sort(alist):
    swapp = True
    while swapp:
        swapp = False
        for i in range(1, len(alist)):
            if alist[i-1] > alist [i]:
                alist[i-1], alist[i] = alist[i], alist[i-1]
                swapp = True
    return alist

print(bubble_sort([192, 12378, 12, -113, 12.5, 10]))
            
def bubble_sort(alist):
    r = []
    while len(alist) > 0:
        m = min(alist)
        r.append(m)
        alist.remove(m)
    return r 
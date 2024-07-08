#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 15:05:51 2022

@author: tiago
"""

def most_frequent(alist):
    freq = {}
    x = 0
    for i in alist:
        freq[i] = freq.get(i, 0) +1
        if freq[i] >= x:
            x = freq[i]
            y = i
    #print(freq)
    return y

"""
def most_frequent(alist):
    alist = sorted(alist, reverse = True)
    r = max(alist, key = alist.count)
    return r
"""
print(most_frequent([-1, 111, 1, 11, -1, 11, 1, 111]))
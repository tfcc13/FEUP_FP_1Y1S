#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 09:21:06 2022

@author: tiago
"""

def sparse_dot_product(dict1, dict2):
    result = 0
    for i in dict1:
        #print(i)
        for j in dict2:
            #print(j)
            if i == j:
                result = result + dict1[i]*dict2[j]
    return result

print(sparse_dot_product({1: 3, 7: 1}, {1: 3, 7: 1}))
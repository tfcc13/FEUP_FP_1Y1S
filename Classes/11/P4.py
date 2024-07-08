#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 11:59:50 2022

@author: tiago
"""

def x_union(list1,list2):
    x = filter(lambda y: y[0] not in list(map(lambda y: y[0],list2)),  list1)
    
    print(list(map(lambda y: y[0],list2)))
    print(list(x))
    
    y = filter(lambda x: x[0] not in list(map(lambda x: x[0],list1)),  list2)
    print(list(map(lambda x: x[0],list1)))
    print(list(y))
    
    return list(x)+list(y)

print(x_union([('a', 1), ('b', 2), ('c',3)], [('d', 4), ('b', 0)]))
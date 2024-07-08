#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 02:08:13 2022

@author: tiago
"""
import functools
def map_filter_reduce(lst,f1,f2,f3):
    return functools.reduce(f3,list(map(f2,filter(f1,lst))))

print(map_filter_reduce([1, 2, 3, 4, 5, 6, 7, 8], lambda i: i % 2 == 0, lambda i: i**2, lambda a, b: a+b))
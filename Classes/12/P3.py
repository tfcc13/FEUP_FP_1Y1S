#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:21:15 2022

@author: tiago
"""

import functools, itertools

def pythagoreans(a,b):
    return ((x,y,z) for x in range(a,b) for y in range(a,b) for z in range(a,b) if x**2+y**2 == z**2 if x < y < z)

print(list(itertools.islice(pythagoreans(1, 10), 10)))
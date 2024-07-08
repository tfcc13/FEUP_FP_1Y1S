#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:00:44 2023

@author: tiago
"""

def evaluate(a, x):
    return sum(map(lambda k: k*(x**a.index(k)), a))

print(evaluate([1, 2, 4], 5))
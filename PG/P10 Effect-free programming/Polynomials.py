#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:17:25 2023

@author: tiago
"""

def evaluate(a, x):
    return sum((k*(x**a.index(k)) for k in a))

print(evaluate([1, 2, 4], 5))

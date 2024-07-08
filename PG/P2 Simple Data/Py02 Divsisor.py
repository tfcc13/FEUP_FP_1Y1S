#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 00:52:22 2022

@author: tiago
"""

n = int(input())
f_sum = 0


for i in range(n+1):
    if i % 3 == 0 or i % 5 == 0:
        f_sum = f_sum + i
print(f_sum)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 01:03:04 2022

@author: tiago
"""

n = int(input())
sum_f = 0

for i in range(1,n+1):
    if n % i == 0:
        sum_f = sum_f + i
print(sum_f)
    
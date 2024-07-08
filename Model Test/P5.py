#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 14:34:47 2022

@author: tiago
"""

a = int(input())
count = 0
decimal = 0
while a > 0:
    n = a % 10
    a = a // 10
    decimal = decimal + n*6**count
    count += 1
    
    
print(decimal)
    

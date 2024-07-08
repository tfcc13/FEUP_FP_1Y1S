#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:47:13 2022

@author: tiago
"""

a = int(input("Insert a 4 digit number!"))
n = 1

for i in range(len(str(a))):
    b = (a // 10**(4-n))*10**(4-n)
    a = a % 10**(4-n)
    n += 1
    print(b)




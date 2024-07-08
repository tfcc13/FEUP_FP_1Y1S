#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:59:48 2022

@author: tiago
"""

a = int(input(""))
half = a // 2
for i in range(a):
    if a % 2 == 0:
        for j in range(a):
            if i <= half and i >=half-1:
                if j <= half and j >=half-1:
                    print("0", end ="")
                else:
                    print("#", end ="")
            else:
                print("#", end ="")
                    
    if a % 2 != 0:
        for j in range(a):
            if i == (half):
                if j == (half):
                    print("0", end ="")
                else:
                    print("#", end ="")
            else:
                print("#", end ="")
    print()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:00:58 2022

@author: tiago
"""

a = int(input())

for i in range(a):
    for j in range(a-i,0,-1):
        print(j, end=" ")
    print()
        
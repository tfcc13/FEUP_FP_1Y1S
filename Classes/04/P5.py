#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 19:28:44 2022

@author: tiago
"""

n1 = int(input())

n2 = int(input())

fin = ""

for i in range(len(str(n1))):
    a = str(n1 % 10)
    b = str(n2 % 10)
    n1 = n1 // 10
    n2 = n2 // 10
    fin = fin + a + b

print(int(fin))
    
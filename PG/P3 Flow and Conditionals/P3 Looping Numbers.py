#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 01:34:24 2022

@author: tiago
"""

n = int(input())
length = len(str(n))


is_looping = True
is_not = False

for i in range(1, length):
    number = n % 10
    n = n // 10
    number2 = n % 10
    n2 = n // 10
    if abs(number2-number) == 1 or (number2==0 and number==9) or (number2==9 and number==0):
        is_looping = True
    else:
        is_looping = False
        is_not = True
        break
print("Looping number"*is_looping+"Not a looping number"*is_not)

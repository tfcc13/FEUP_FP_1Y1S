#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 02:07:20 2022

@author: tiago
"""




num = int(input())
    
final = 0
check = True

for i in range(len(str(num))):
    if num % 10 < 8:
        octal = num % 10
        final = final + octal * 8**i
        num = num //10
    else:
        check = False
        print("Not a valid number.")
        break
if check == True:
    print(final*check)
    




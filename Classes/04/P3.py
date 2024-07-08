#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 10:02:29 2022

@author: tiago
"""

numb = int(input("insert a digit"))
if numb >= 0:
    length = len(str(numb))
else:
    length = len(str(numb))-1  

final = 0

if numb >= 0:
    for i in range(len(str(numb))):
        digit = numb % 10
        final = final + digit * 10  ** (length-1-i)
        numb = numb // 10
    
    print(final)
else:
    numb = abs(numb)
    for i in range(len(str(numb))):
        digit = numb % 10
        final = final + digit * 10  ** (length-1-i)
        numb = numb // 10
    
    print(final*-1)

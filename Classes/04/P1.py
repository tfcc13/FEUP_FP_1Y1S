#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 08:35:49 2022

@author: tiago
"""


numb =int(input(""))

if numb>0:
    for i in range(1,11):
        if i < numb:
            outcome = numb*i
            print(f"{numb} x {i} = {outcome}" )
        elif i == numb:
            outcome = (numb)**2
            i = i-1
            print(f"{numb} ^ {2} = {outcome}")
        elif i > numb:
            break
else:
    for i in range(1,11):
            outcome = numb*i
            print(f"{numb} x {i} = {outcome}" )
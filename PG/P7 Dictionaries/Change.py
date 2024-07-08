#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 15:57:33 2022

@author: tiago
"""

def change(money):
    
    dict1 = {2.0: 0, 1.0: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}
    for i in dict1.keys():
        x = money / i
        dict1[i] = int(x)
        money = round(money - i*int(x),3)
        print(money)
                
    return dict1

print(change(5.23))
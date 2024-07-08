#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:19:46 2022

@author: tiago
"""

def next_leap_year(y):
    y = y+1
    
    while True:
        if (y % 400 == 0 and y %100 == 0) or (y % 4 == 0 and y %100 != 0) :
            return y
        
        y+=1


print(next_leap_year(2004))
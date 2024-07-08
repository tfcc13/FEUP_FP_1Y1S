#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 20:52:59 2022

@author: tiago
"""

def square_odds(values):
    x = [str(int(x)*int(x)) for x in values.split(",") if int(x)%2 != 0]
    return ",".join(x)
        
    
print(square_odds("1,2,3,4,5,6,7,8,9"))

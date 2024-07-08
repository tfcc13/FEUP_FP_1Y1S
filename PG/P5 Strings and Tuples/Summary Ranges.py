#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 14:57:15 2022

@author: tiago
"""

def summary_ranges(a_string):
    start = 0
    x = a_string.split(",")

    result = ""

    for i in range(len(x)):
        if i+1 < len(x) and int(x[i]) +1 == int(x[i+1]):
            continue
        
        if start == i:
            result = result +str(x[start]) +","
        else:
            result = result + str(x[start]) + "->" + str(x[i])+","
         
        start = i + 1            
            
    return result [:-1]


print(summary_ranges('1,3,4,6,7,9,10'))
        
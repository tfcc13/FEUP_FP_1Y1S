#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:12:27 2022

@author: tiago
"""


number = float(input())
lower = 0 
upper = number
midpoint = (upper+lower)/2


while  upper-lower > 0.00001:
    if midpoint*midpoint == number:
        break
    if midpoint*midpoint > number:
        upper = midpoint
    elif midpoint *midpoint < number:
        lower = midpoint
    midpoint = (upper+lower)/2
    
print(round(midpoint,5))
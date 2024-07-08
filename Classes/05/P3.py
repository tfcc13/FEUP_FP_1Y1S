#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 09:37:58 2022

@author: tiago
"""

def var_numbers(number, precision=2):
    sumf = 0   
    count = 0
    sums = 0
    for i in range(1,number+1):
       sumf = sumf + i
       count +=1
    avg = sumf/count
    
    for i in range(1, number+1):
        sums = (sums + (i-avg)**2)
    variance = sums/number
    return (round(variance,precision))

(var_numbers(10,1))
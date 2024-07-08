#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 08:56:14 2022

@author: tiago
"""

def calc_triangular(n):
    sum = 0
    for i in range(n+1):
        sum = sum + i
    return sum

calc_triangular(10)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 14:15:49 2022

@author: tiago
"""

import math

def compute_euler(x):
    fsum = 0
    for i in range(x+1):
        fsum = fsum + 1/math.factorial(i)
    return round(fsum,5)
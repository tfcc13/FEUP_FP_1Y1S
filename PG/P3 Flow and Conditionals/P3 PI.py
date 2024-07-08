#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:56:57 2022

@author: tiago
"""

import math

k = 50
cons = 2*math.sqrt(2)/9801
sum_k = 0

for i in range(k+1):
    a = math.factorial(4*i)*(1103+26390*i)
    b = ((math.factorial(i))**4)*(396**(4*i))
    sum_k = sum_k + a/b
pi = 1/(cons*sum_k)

print(round(pi,8))
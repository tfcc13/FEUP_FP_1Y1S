#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:13:50 2022

@author: tiago
"""
import math

def deriv(f):
    def derivada(x):
        h = 0.001
        return round((f(x+h)-f(x))/h,3)
        
    return derivada
    
def f(x):
    return x*x + 2*x + 2

print(deriv(f)(3))    
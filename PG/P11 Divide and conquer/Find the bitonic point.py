#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 15:04:09 2023

@author: tiago
"""

def bitonic_point(f):
    
   return (i for i in range(1,len(f())) if f()[i-1] < f()[i] > f()[i+1])
            

print(bitonic_point(lambda: [2, 6, 10, 25, 60, 30, 25, 10, 0]))


def bitonic_point(f):
    
   return max(f())

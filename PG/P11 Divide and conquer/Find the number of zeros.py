#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 15:14:30 2023

@author: tiago
"""

def count_zeros(f):
    
    return f().count(0)

print(count_zeros(lambda: [1, 1, 1, 0, 0]))
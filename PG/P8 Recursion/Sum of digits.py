#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 15:31:59 2022

@author: tiago
"""

def sum_digits_rec(n):
    
    if n < 10:
        return n
    return n % 10 + sum_digits_rec(n//10)

print(sum_digits_rec(12))
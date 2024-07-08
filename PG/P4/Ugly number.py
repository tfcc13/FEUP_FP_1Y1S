#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 14:53:23 2022

@author: tiago
"""

def ugly(n):

    if n % 5 == 0:
        n = n/5
    if n % 3 == 0:
        n = n/3
    if n % 2 == 0:
        n = n/2
    return n == 1
        

print(ugly(6))
        
        
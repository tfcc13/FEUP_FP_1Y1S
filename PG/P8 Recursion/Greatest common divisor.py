#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 15:02:35 2022

@author: tiago
"""


def gcd_rec(n1, n2):

    if n2 >0:
        return gcd_rec(n2,n1%n2)
    return n1
        
print(gcd_rec(13, 21))
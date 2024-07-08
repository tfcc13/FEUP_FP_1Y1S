#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 14:36:41 2022

@author: tiago
"""

def genbin(bit_count):
    binstr = []
    def genbin2(n, bs=''):
        if len(bs) == n:
            binstr.append(bs)
        else:
            genbin2(n, bs + '0')
            genbin2(n, bs + '1')


    genbin2(bit_count)
    return binstr

def check1(n):
    if "11" in n:
        return False
    else:
        return True

def no_consecutives1(k):
    lista = genbin(k)
    count = list(filter(check1, lista))
    
    return len(count)
    

""" def no_consecutives1(k):
    if k == 1:
        return 2
    elif k == 0:
        return 1
    else:
        return no_consecutives1(k - 2) + no_consecutives1(k - 1)
    """
print(no_consecutives1(3))
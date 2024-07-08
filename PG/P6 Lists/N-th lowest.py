#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 16:12:37 2022

@author: tiago
"""

def nth_lowest(lnum,n):
    lista = []
    for i in range(n):
        x = min(lnum)
        lista.append(x):
        lnum.remove(x)
    
    return max(lista)
                
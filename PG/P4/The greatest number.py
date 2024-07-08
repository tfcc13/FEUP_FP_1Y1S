#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 12:38:39 2022

@author: tiago
"""

def greatest(num):
    lista = []
    final = 0
    while num > 0:
        n = num % 10
        num = num // 10
        lista.append(n)
    lista = sorted(lista)
    
    for i, number in enumerate(lista,start=0):
        final = final + number * 10 ** i
        
    return final

print(greatest(310909))
        
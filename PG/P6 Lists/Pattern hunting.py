#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 18:04:08 2022

@author: tiago
"""

def pattern_hunting(l1,l2,p):
    lista1 = []
    lista2 = []
    resultado = []
    count = 0
    for i in range(len(l1)):
        if p in l1[i]:
            lista1.append(i)
            resultado.append(l2[i])
        if p in l2[i]:
            lista2.append(i)
            resultado.append(l1[i])
    return sorted(resultado, reverse=True)


            
print(pattern_hunting(['a string', 'two strings', 'not here'], ['choose me', 'me too', 'but not me'], 'string'))
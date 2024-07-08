#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:50:36 2022

@author: tiago
"""
import string
"""def longest(s):
   lista = []
    
    result = ""
    for i in s:
        if i.isalpha():
            result = result+i
        if not i.isalpha():
            lista.append(result)
            result = ""
    lista.append(result)
    
    maior = ""
    for i in lista:
        if len(i) > len(maior):
            maior = i
            


        
    return len(maior)"""

def longest(s):
    lista = s.split()
    return len(max(lista, key = len))
    

print(longest("Unnecessarily long sentence since the longest word is the first one"))                
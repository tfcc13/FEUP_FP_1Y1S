#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:35:19 2022

@author: tiago
"""
def uncommons(s1,s2): # Usando dicionários
 
    res = ""
    map = {}
    
    for ch in s2:
        map[ch] = 1
        
    for ch in s1:
        if ch not in map:
            res = res + ch
        else:
            map[ch] = 2
    
    for ch in s2:
        if map[ch] == 1:
            res = res +ch
            
    
    return res
    

print()
s1 = "abcs"
s2 ="cxzca"

print(uncommons(s1, s2))

def uncommons1(s1,s2):
    
    set1 = set(s1)
    set2= set(s2)
    
    uncommon = list(set1^set2)
    
    return "".join(uncommon)

print(uncommons1(s1, s2))
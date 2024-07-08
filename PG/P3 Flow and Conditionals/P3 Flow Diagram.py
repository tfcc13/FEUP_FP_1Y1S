#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 18:28:47 2022

@author: tiago
"""

L = int(input())
S = int(input())

R = L

if R <= S:
    L = R
    R = S
    S = L

while S <= R:
    R = R-S
    
while R!= 0:
    L = R
    R = S
    S = L
    while S <= R:
        R = R-S
        
print(S)
    
    
    
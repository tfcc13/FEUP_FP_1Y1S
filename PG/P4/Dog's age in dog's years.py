#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:31:53 2022

@author: tiago
"""

def dogs(h_age):
   
    check = h_age >2
    check2 = h_age <= 2 and h_age > 0
    fst = 10.5 * h_age 
    rest = 4 * (h_age-2) + 10.5*2
    
    return check * rest + check2*fst

print(dogs(3))
    
    
    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 09:00:37 2022

@author: tiago
"""
def adigits(a,b,c):
    pos1 = min(a,b,c)
    pos3 = max(a,b,c)
    pos2 = a+b+c-pos1-pos3
    
    return pos1*100+pos2*10+pos3
    
    
print(adigits(0,1,0))
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 11:39:24 2022

@author: tiago
"""





def variance(alist):
    global avg
    avg = sum(alist)/len(alist)
    return round(sum(map(aux,alist))/len(alist),3)
    
    
    
def aux(x):
   
    return (x-avg)**2

print(variance([1, 2, 3, 4, 5, 6]))
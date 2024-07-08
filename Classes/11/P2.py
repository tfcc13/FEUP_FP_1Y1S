#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 11:15:36 2022

@author: tiago
"""

def differences(alist):
    
    
    x = zip(alist[1:],alist)
    return list(map(aux, x))

def aux(tup):
    return tup[0] - tup[1]
print(differences([1, 2, 3, 4]))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 22:19:46 2022

@author: tiago
""import operator

def distribute(adict, op):
    for x in adict.keys():
        if adict[x] != []:
            for y in adict[x]:
                yield op(x,y)
        else:
            yield x
    
print(list(distribute({1:[0.1,0.5], 2:[], 3:[0,0.75]}, operator.add)))"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 21:24:14 2022

@author: tiago
"""

def multi(g):
    
    tuplo = ()
    tuplofinal = ()
    for i in g:
        count = g.count(i)

        tuplo += ((i[0], count, i[1]),)
    for i in tuplo:
        if i not in tuplofinal:
            tuplofinal += (i,)
    
    return tuplofinal

print(tuple(sorted(multi((('A','B'),('A','C'),('B','C'),('C','B'),('A','B'))))))
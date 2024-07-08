#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 17:29:13 2022

@author: tiago
"""

def unique_ntree(tree):
    lista = []
    
    if type(tree) == int:
        lista.append(tree)
        return lista
    if tree == ():
        return []
    if type(tree) == tuple:
        return sorted(list(set((unique_ntree(tree[1]) +unique_ntree(tree[0]) +unique_ntree(tree[2])))))
    
        
    
        
    
print(unique_ntree((1, (2, (), ()), (1, (), ()))))
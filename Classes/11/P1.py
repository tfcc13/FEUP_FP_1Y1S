#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 10:59:06 2022

@author: tiago
"""

def sort_pairs(alist):
    return sorted(alist, key= lambda x: (x[1],x[0]))
    
print(sort_pairs([("Catarina", 18), ("Bruno", 19), ("Beatriz", 19)]))

	


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 14:32:20 2023

@author: tiago
"""

import statistics

def batch_norm(alist, batch_size):

    for x in batchs(alist, batch_size):

        yield[i- statistics.median(x) for i in x]
        
        
def batchs(alist, batch_size):
    for i in range(0, len(alist), batch_size):
        yield alist[i:i+batch_size]
        
print(list(batch_norm([-1, 0, 1, 1, 2, 4], 3)))

print(list(batch_norm( 	[10, 1, -12, 5, 1, 3, 7, 3, 3], 5)))

import statistics

def batch_norm(alist, batch_size):
    for i in range(0, len(alist), batch_size):
        batch = alist[i:i + batch_size]
        median = statistics.median(batch)
        norm_batch = list(map(lambda x: x - median, batch))
        yield norm_batch
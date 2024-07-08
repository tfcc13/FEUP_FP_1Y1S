#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 09:45:51 2022

@author: tiago
"""

def msort(xs):
    if len(xs) <= 1:
        return xs
    
    n = len(xs) // 2
    xs1 = msort(xs[:n])
    xs2 = msort(xs[n:])
    return merge(xs1,xs2)
    
        
    
    
    
def merge(xs,ys):
   result = []
   xi = 0   # i-th element of xs
   yi = 0   # i-th element of ys

   while True:
       if xi >= len(xs):           # If xs list is finished,
           result.extend(ys[yi:])  # Add remaining items from ys
           return result           # And we're done.

       if yi >= len(ys):           # Same again, but swap roles
           result.extend(xs[xi:])
           return result

       # Both lists still have items, copy smaller item to result.
       if xs[xi] <= ys[yi]:
           result.append(xs[xi])
           xi += 1
       else:
           result.append(ys[yi])
           yi += 1
        
print(msort([3, 2, 1, 4]))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 14:09:10 2023

@author: tiago
"""

def permuta(alist, step=0):
    res = []
    
    if step == len(alist)-1:
        res.append(alist)
    
    for i in range(step,len(alist)):
        cp = alist.copy()
        cp[i],cp[step] = alist[step], alist[i]
        res += permuta(cp,step+1)
        
    return res

print(permuta(['A', 'B', 'C']))


def permuta(alist, step=0):
    # Check if the step is equal to the length of the list
    if step == len(alist):
        # If the step is equal to the length of the list, return a list containing
        # the permuted list
        return [alist[:]]
    else:
        # If the step is smaller than the length of the list, initialize an empty list
        # to store the permutations
        perms = []
        
        # Iterate over the elements of the list
        for i in range(step, len(alist)):
            # Swap the element at index step with the element at index i
            alist[step], alist[i] = alist[i], alist[step]
            
            # Compute the permutations of the permuted list and add them to the list
            # of permutations
            perms.extend(permuta(alist, step + 1))
            
            # Swap the elements back to their original positions
            alist[step], alist[i] = alist[i], alist[step]
        
        # Return the list of permutations
        return perms
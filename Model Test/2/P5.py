#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 18:21:10 2022

@author: tiago
"""

def magic_square(n):

    dict1 = {}
    cols = []
    u = 1
    for i in range(n):
        for k in range(n):
            dict1[(i,k)] = dict1.get((i,k),0)
    print(dict1)
    
    i,j = 0, n // 2
    
    while u <= n**2: 
        dict1[(i,j)] = u
        u += 1
        o,p = i,j
        i,j = check_boundaries(i-1, j+1, n)
        
        if dict1.get((i,j)) != 0:
            i,j = check_boundaries(o+1,p,n)

    for t in range(n):
        rows = []
        for k in range(n):
            rows.append(dict1[(t,k)])
        cols.append(rows)
            
        
        
        
        
    return cols
            
    
def check_boundaries(i,j,n):
    if i > n-1:
        i = 0
    if j > n-1:
        j = 0
    if i < 0:
        i = n-1
    if j < 0:
        j = n-1
    return i,j
        
            

"""
def magic_square(n):
    
    assert n>=1 and n%2 == 1
    # create an empty square
    square = []
    for i in range(n):
        square.append([0]*n)
    # fill in the numbers
    i = 0
    j = n//2
    k = 1
    while k <= n*n:
        if square[i][j] == 0:  # empty
            square[i][j] = k
            k = k+1
            i = (i-1) % n
            j = (j+1) % n
        else:
            i = (i+2) % n
            j = (j-1) % n
    return square
"""
print(magic_square(3))
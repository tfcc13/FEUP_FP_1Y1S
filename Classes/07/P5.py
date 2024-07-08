#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 14:05:32 2022

@author: tiago
"""

def mult(M,N):
    colM = len(M[0])
    rowN = len(N)
    colN = len(N[0])
    rowM = len(M)
    count = 0
    count1 = 0
    resultado = []
    if colM != rowN:
        return []
    
    for i in range(rowM):
        temp = []
        for j in range(colN):
            total = 0
            for k in range(colM):
                total += M[i][k] * N[k][j]
            temp.append(total)
        resultado.append(temp)
    return resultado
        
        
        
        



print(mult([[1, 2], [3, 4]], [[2, 0], [1, 2]]))
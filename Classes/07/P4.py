#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:41:44 2022

@author: tiago
"""

def magic(mat):
    soma = 0
    rows = len(mat)
    col = len(mat[0])
    teste = 0
    
    for i in range(col):
        teste += mat[0][i]
    
    #Rows
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            soma = soma+mat[i][j]
        if soma == teste:
            soma = 0
        else:
            return False


    #Columns
    count = 0
    soma1 = 0
    n1 = 1
    
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            soma1 = soma1+mat[j][i]
        if soma1 == teste:
            soma1 = 0
        else:
            return False


#1st diag
    count = 0
    soma3 = 0   
    for i in range(rows):
        soma3 = soma3+mat[i][count]
        count += 1
    if soma3 == teste:
        soma3 = 0
    else:
        return False

# Reverse diag

    count = 0 
    soma4 = 0   
    for i in range(col-1,-1,-1):
        soma4 = soma4 + mat[count][i]
        count += 1
    if soma4 == teste:
        soma4 = 0
    else:
        return False
    

    return soma==soma1==soma3==soma4

 	

print(magic([[1, 0, 2], [1, 0, 2], [1, 0, 2]]))
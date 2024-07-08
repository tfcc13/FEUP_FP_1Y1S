#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 11:58:19 2022

@author: tiago
"""

def vizinhanca(m, w, line, col):

    if w == '':
        return True
    if line < 0 or line >= len(m) or col < 0 or col >= len(m[0]):
        return False
    if m[line][col] == w[0]:
        
        if vizinhanca(m, w[1:], line+1, col):
            return True
        if vizinhanca(m, w[1:], line, col+1):
            return True
        if vizinhanca(m, w[1:], line-1, col):
            return True
        if vizinhanca(m, w[1:], line, col-1):
            return True
    return False
 
def soup(matrix, word):

    for line in range(len(matrix)):
        for col in range(len(matrix[0])):
            if vizinhanca(matrix, word, line, col):
                return f"{chr(ord('A') + line)}{col+1}"
print(soup([['X', 'R', 'Z', 'B', 'H', 'A'], ['K', 'A', 'S', 'I', 'G', 'O'], ['J', 'O', 'T', 'C', 'A', 'N'], ['F', 'S', 'R', 'H', 'T', 'U'], ['D', 'P', 'O', 'O', 'X', 'F'], ['Z', 'B', 'B', 'W', 'F', 'S']], 'PORTO'))

	


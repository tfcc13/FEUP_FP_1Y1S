#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:29:15 2023

@author: tiago
"""

def four_in_line(board):
    
    w = set()
    
    for c in range(len(board[0])-3):
        for r in range(len(board)):
            if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] != 0:
                w.add((r,c))
                w.add((r, c+3))
                
    for c in range(len(board[0])):
        for r in range(len(board)-3):
            if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c] != 0:
                w.add((r,c))
                w.add((r+3,c))
                
    for c in range(len(board[0])-3):
        
        for r in range(len(board)-3):
            if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3] != 0:
                w.add((r,c))
                w.add((r+3,c+3))
                
    for c in range(len(board[0])-3):
        for r in range(3, len(board)):
            if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3] != 0:
                w.add((r,c))
                w.add((r-3,c+3))
                    
    return w

print(four_in_line( 	[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 2, 0, 0], [0, 0, 2, 2, 0], [0, 1, 1, 1, 1], [0, 1, 1, 1, 2]]))


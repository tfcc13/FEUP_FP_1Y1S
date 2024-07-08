#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:35:35 2023

@author: tiago
"""

def tic_tac_toe(board, player):
    board = [list(row) for row in board.splitlines()]
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = player
                if check_win(board, row, col, player):
                    return chr(ord("A")+row)+str(col+1)

def check_win(board, row,col, player):
    
    w_col = "".join([r[col] for r in board]) == player*3
    
    w_row = "".join(board[row]) == player*3

    w_diag1 = "".join(board[i][i] for i in range(3)) == player*3

    w_diag2 = "".join([board[i][2-i] for i in range(3)]) == player* 3
    
    return w_col or w_row or w_diag1 or w_diag2
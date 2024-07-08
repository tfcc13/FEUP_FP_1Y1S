#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:33:47 2022

@author: tiago
"""


grid =              [[3,0,0,8,0,0,0,0,1],
                    [0,0,0,0,0,2,0,0,0],
                    [0,4,1,5,0,0,8,3,0],
                    [0,2,0,0,0,1,0,0,0],
                    [8,5,0,4,0,3,0,1,7],
                    [0,0,0,7,0,0,0,2,0],
                    [0,8,5,0,0,9,7,4,0],
                    [0,0,0,1,0,0,0,0,0],
                    [9,0,0,0,0,7,0,0,6]]

def solve():
    
    """Solve the Sudoku Puzzle"""
    global grid
    #Find zeros in the grid
    zeros = []
    
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                zeros.append((row,col))
    solve_rec(zeros)
    
def solve_rec(zeros):
    """Solve the Sudoku puzzle recursively"""
    
    if len(zeros) == 0:
        #Finished
        print(grid)
        
    else:
        # recursive case
        (row,col) = zeros[0]
        for number in range(1,10):
            # place numnber at row,col if possible
            if check_possible(number, row,col):
                #place number and recursively continue
                grid[row][col] = number
                solve_rec(zeros[1:])
                grid[row][col] = 0
        print_solution()
            
def check_possible(number,row,col):
    """ Check if we can place number at row,col"""
    global grid
    #Check if the number occurs in the line
    
    for i in range(9):
        if grid[row][i] == number:
            return False
        if grid[i][col] == number:
            return False
        
    # Check the subsquare
    
    r = (row//3)*3
    c = (col//3) * 3
    for i in range(3):
        for j in range(3):
            
            if grid[r+i][c+j] == number:
                return False
            
    return True

def print_solution():
    
    global grid
    print(40*"-")
    print("Solution:")
    for row in grid:
        print(row)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 09:50:51 2022

@author: tiago
"""

    
def mastermind(g1, g2, g3, c1, c2, c3):
    points = 0

    if g1 == c1:
        points += 3
        g1 = 1
        c1 = 0
    if g2 == c2:
        points += 3
        g2 = 1
        c2 = 0
    if g3 == c3:
        points += 3
        g3 = 1 
        c3 = 0
    if g1 == c2:
        points +=1
        g1 = 1
        c2 = 0
    if g1 == c3:
        points += 1
        g1 = 1
        c3 = 0
    if g2 == c1:
        points += 1
        g2 = 1
        c1 = 0
    if g2 == c3:
        points += 1
        g2 = 1
        c3 = 0
    if g3 == c1:
        points += 1
        g3 = 1
        c1 = 0
    if g3 == c2:
        points += 1
        g3 = 1
        c2 = 0
    return points

 	

print(mastermind("b", "b", "y", "y", "y", "b"))
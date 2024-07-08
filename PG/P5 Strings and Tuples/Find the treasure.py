#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:14:19 2022

@author: tiago
"""

def map(pos, steps):
    lista = steps.split("-")
    up = (steps.count("up"))
    left = -(steps.count("left"))
    right = (steps.count("right"))
    down = (-steps.count("down"))
    print(steps.count("up"))
    print(lista)
    return (pos[0]+left+right, pos[1] + up+down)

print(map((0, 0), 'up-up-left-right-up-up'))
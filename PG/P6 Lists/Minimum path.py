#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 16:43:25 2022

@author: tiago
"""

def min_path(path):
    resultado = []
    upcount = path.count("UP")
    downcount = path.count("DOWN")
    leftcount = path.count("LEFT")
    rightcount = path.count("RIGHT")
    
    if upcount == downcount == rightcount == leftcount:
        return path

    for i in path:
        if i == "RIGHT" and rightcount > leftcount:
            resultado.append(i)
            rightcount -= 1
            continue
        if i == "LEFT" and leftcount > rightcount:
            resultado.append(i)
            leftcount -=1 
            continue
        if i == "UP" and upcount > downcount:
            resultado.append(i)
            upcount -=1 
            continue
        if i == "DOWN" and downcount > upcount:
            resultado.append(i)
            downcount -= 1
            continue
  
        
        
            
    return resultado

    




print(min_path(['LEFT', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'UP', 'LEFT']))
print(min_path(['UP', 'DOWN', 'UP', 'LEFT', 'RIGHT']))
print(min_path(['UP', 'LEFT', 'DOWN', 'RIGHT']))
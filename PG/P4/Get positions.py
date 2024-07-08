#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:24:06 2022

@author: tiago
"""

def get_positions(x,y):
    pos = ""
    lista = x.split(" ")
    count = 0 
    
    for i in lista:
        for num,j in enumerate(y):
            if i == j:
                pos = pos + " " + str(num)
                count +=1
    count = count > 1
    return pos*count

print(get_positions('dinosaur goodbye', ['goodbye', 'hello', 'breakfast']))
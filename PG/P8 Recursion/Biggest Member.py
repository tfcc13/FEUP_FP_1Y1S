#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 15:36:42 2022

@author: tiago
"""


def biggest_member(atuple):

    for i in atuple:
        if type(i) == tuple:
                atuple = max(biggest_member(i),atuple, key=len)
    return atuple
    
    
        
        

print(biggest_member((1, (5, (6, 8), 3, 9), 2)))
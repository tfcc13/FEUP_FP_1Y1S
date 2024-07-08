#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 09:24:33 2023

@author: tiago
"""

# def generator(intlist):
#     result= []
#     for x in intlist:
#         i,f = x
#         result += (k for k in range(i,f+1))
#     for l in result:
#         yield l
        


def generator(intlist):
    
    for element in intlist:
        
        yield (i for i in range(element[0], element[1]+1)) 
    
print((generator([(1, 1), (3, 5), (10, 15)])))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 12:39:13 2022

@author: tiago
"""

import functools

def bounding_box(pts):
    xmin = pts[0][0]
    ymin = pts[0][1]
    xmax = pts[0][0]
    ymax = pts[0][1]
    xmin = functools.reduce(smallerx,map(lambda x: x[0],pts))
    ymin = functools.reduce(smallery,map(lambda y: y[1],pts))
    xmax = functools.reduce(biggerx,map(lambda x: x[0],pts))
    ymax = functools.reduce(biggery,map(lambda y: y[1],pts))
    
    

    return xmin, ymin, xmax,ymax

def smallerx(x,xmin):
    if x < xmin:
        return x
    else:
        return xmin
def biggerx(x, xmax):
    if x > xmax:
        return x
    else:
        return xmax

def smallery(y, ymin):
    if y < ymin:
        return y
    else:
        return ymin
def biggery(y, ymax):
    if y > ymax:
        return y
    else:
        return ymax    

print(bounding_box([(1,0), (1,1), (0,0), (-1,0), (0,-1)]))
print(bounding_box([(0,0), (1,1), (2,2), (3,3)]))
print(bounding_box([(1,1)]))

"""
import functools

def bounding_box(pts):
    xmin = functools.reduce(min,map(lambda x: x[0],pts))
    ymin = functools.reduce(min,map(lambda y: y[1],pts))
    xmax = functools.reduce(max,map(lambda x: x[0],pts))
    ymax = functools.reduce(max,map(lambda y: y[1],pts))
    
    

    return xmin, ymin, xmax,ymax """
    
    
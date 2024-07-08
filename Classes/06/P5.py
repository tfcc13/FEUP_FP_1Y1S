#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 22:43:49 2022

@author: tiago
"""

def triplet(x):
    triptup =()
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            for k in range(j+1,len(x)):
                if x[i]+x[j]+x[k] == 0:
                    triptup += (x[i],x[j],x[k])
                    return triptup
    return triptup

print(triplet((-1, 1, 1, 1)))
        
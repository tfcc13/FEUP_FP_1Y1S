#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:40:24 2022

@author: tiago
"""

def count_until(tup):
    count = 0
    for i in tup:
        if type(i)==tuple:
            return count
        count += 1
    return -1
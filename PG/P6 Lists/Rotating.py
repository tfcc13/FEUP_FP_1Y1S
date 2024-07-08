#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 16:20:21 2022

@author: tiago
"""

def rotate_list(l):
    return l[3:]+l[:3]

print(rotate_list([9, 8, 2]))
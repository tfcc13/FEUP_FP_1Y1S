#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 01:55:46 2022

@author: tiago
"""

def to_celsius(t):
    return list(map(lambda x: round((x-32)*5/9,1),t))

print(to_celsius([84.56, 79.7, 81.14, 82.4, 82.04]))
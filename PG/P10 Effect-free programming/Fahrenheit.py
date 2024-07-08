#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:20:36 2023

@author: tiago
"""


def to_fahrenheit(t):
    return list(round(((f*1.8)+32), 2) for f in t)

print(to_fahrenheit([29.2, 26.5, 27.3, 28, 27.8]))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 10:26:18 2022

@author: tiago
"""

p = float(input())
r = float(input())
n = float(input())
t = 2

A = p * (1+(r/n))**(n*t)

print(round(A,3))
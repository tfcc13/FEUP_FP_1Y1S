#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 01:39:40 2022

@author: tiago
"""

def paint(n, boards):
    if n == 1:
        return max(boards)
    else:
        l = []
        for i in range(1, len(boards) - n + 2):
            v = max(boards[:i]) + paint(n - 1, boards[i:])
            l.append(v)
        return min(l)
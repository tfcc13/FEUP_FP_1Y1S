#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 12:50:51 2023

@author: tiago
"""

def last_man_standing(alist, step):
    if len(alist) == 1:
        return alist[0]
    elif len(alist) > 0:
        cp = alist.copy()
        a = alist.pop((step-1) % len(alist))
        alist= alist[cp.index(a):] + alist[:cp.index(a)]
        return last_man_standing(alist, step)

    
print(last_man_standing(['I', 'II', 'III'], 6))
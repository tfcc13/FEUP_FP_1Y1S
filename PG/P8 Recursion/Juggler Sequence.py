#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 15:23:20 2022

@author: tiago
"""

def juggler(n,p):
    if p == 0:
        return n
    else:
        if juggler(n,p-1) % 2 == 0:
            return int(juggler(n, p-1)**0.5)
        elif juggler(n,p-1)%2 != 0:
            return int(juggler(n, p-1)**(3/2))
            
"""
def juggler(n, p):
    if p == 0:
        return n

    return int(juggler(n, p - 1) ** (((n % 2 == 0) + 3 * (n % 2 != 0)) / 2))
"""
    
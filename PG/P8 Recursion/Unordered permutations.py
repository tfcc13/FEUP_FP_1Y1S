#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:31:22 2022

@author: tiago
"""


def permutations(atuple):
    if len(atuple) == 1:
        return {atuple}
    else:
        result = set()
        for i in range(len(atuple)):
            for s in permutations(atuple[:i] + atuple[i+1:]):
                new = (atuple[i],) + s
                result |= {new}
    return result
        
print(permutations(('hello', 'world')))
print(permutations(('A', 'B', 'C')))
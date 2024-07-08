#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 00:17:17 2022

@author: tiago
"""

def preorder(tree):
    result = []
    if type(tree) != tuple:
        return []
    result.append(tree[0])
    result += preorder(tree[1])
    result += preorder(tree[2])
    return result
print(preorder((1, (2, None, None), (3, None, None))))
print(preorder((2, (7, (2, None, None), (6, (5, None, None), (11, None, None))), (5, None, (9, (4, None, None), None)))))
            
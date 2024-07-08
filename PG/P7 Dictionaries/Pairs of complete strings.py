#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 02:12:37 2022

@author: tiago
"""
def complete_pairs(s1,s2):
    x = "abcdefghijklmnopqrstuvwxyz"
    set1 = set()
    for i in s1:
        for j in s2:
            if set(i+j) == set(x):
                set1.add(i+j)
        #print(sorted(i+j))
    return set1

print(complete_pairs({'abc', 'lmnopqrst', 'abcdefgh', 'geeksforgeeks'}, {'ijklmnopqrstuvwxyz', 'defghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'}))
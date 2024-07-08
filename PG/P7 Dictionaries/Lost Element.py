#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 13:28:12 2022

@author: tiago
"""



	

def lost_element(s1, s2):
    return (max(s1,s2)-min(s1,s2)).pop()

print(lost_element({1, 4, 5, 7, 9}, {9, 4, 5, 7}))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:32:24 2022

@author: tiago
"""
import string

def count_chars(a_string):
    count = 0
    count1 = 0
    count2 = 0
    for i in a_string:
        if i in string.ascii_letters:
            count += 1
        elif i in "0123456789":
            count1 +=1
        else:
            count2 += 1
    return (count,count1,count2)

print(count_chars('Hello-2019-World'))
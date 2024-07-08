#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:22:40 2022

@author: tiago
"""

def count_chars(sentence,letter):
    count = 0
    for i in sentence:
        if i == letter:
            count += 1
    return count

print(count_chars('Eddie edited it', 't'))
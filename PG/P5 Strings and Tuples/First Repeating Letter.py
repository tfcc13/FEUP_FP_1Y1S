#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:21:50 2022

@author: tiago
"""

def repeated_letter(s):
    for i in s:
        for k in s[1::]:
            if i == k:
                return i
        if s == []:
            return None
        s = s[1::]
        
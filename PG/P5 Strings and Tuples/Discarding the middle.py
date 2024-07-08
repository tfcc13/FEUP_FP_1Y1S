#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:43:44 2022

@author: tiago
"""

def discard_middle(s):
    
    if len(s) <4:
        return ""
    return s[0:2]+s[-2:len(s)]
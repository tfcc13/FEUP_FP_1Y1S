#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:03:01 2022

@author: tiago
"""

def validate(x):
    return (type(x) == float or type(x)== int) and (x >= 0 and x <= 100)

print(validate("f"))
    
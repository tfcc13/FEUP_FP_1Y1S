#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:00:08 2022

@author: tiago
"""

import math
import string

def caesar(n):
    message = ""
    for p,i in enumerate(n):
        print(p)
        index = ord(i)-ord("A")
        fn = ((1+math.sqrt(5))**p-(1-math.sqrt(5))**p)/(math.sqrt(5)*2**p)
        new_index = (index - int(fn)) % 26
        char_num = new_index + ord("A")
        if i in string.ascii_uppercase:
            message = message + chr(char_num)
        else:
            message = message + i
    return message

print(caesar("HELLO WORLD!"))
            
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 01:11:45 2022

@author: tiago
"""
import math

LE = int(input())
RE = int(input())
PE = int(input())
TE = int(input())


if LE < 0 or LE > 100 or RE > 100 or RE < 0 or PE > 100 or PE < 0 or TE > 100 or TE <0:
    print("Input error")
elif PE >= 40 and TE >= 40:
    grade = (LE+RE+13*PE+5*TE)/100
    if (grade * 10)%100 >= 5:
        print(math.ceil(grade))
    else:
        print(math.floor(grade))
else:
    print("RFF")
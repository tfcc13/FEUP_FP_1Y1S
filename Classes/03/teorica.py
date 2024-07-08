#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 10:31:41 2022

@author: tiago
"""
import math

a = int(input("a"))
b = int(input("b"))
c = int(input("c"))


if a == 0:
    print("Go away")
else:
    dis = (b*b - 4 * a* c)
    sqr_dis = math.sqrt(abs(dis))
    if dis > 0:
        print("first root", (-b + sqr_dis)/(2*a))
        print("second root", (-b - sqr_dis)/(2*a))
    elif dis == 0:
        print("second root", -b / 2*a)
    else: 
        print("First root", -b/(2*a), "+j", sqr_dis)
        print("First root", -b/(2*a), "+j", sqr_dis)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:11:40 2022

@author: tiago
"""

def change(amount):
    troco = []
    while amount > 0:
        if amount >= 200:
            amount = amount - 200
            troco.append(200)
        if 200 > amount >= 100:
            amount = amount - 100
            troco.append(100)
        if 100 > amount >= 50:
            amount = amount - 50
            troco.append(50)
        if 50 > amount >= 20:
            amount = amount - 20
            troco.append(20)
        if 20 > amount >= 10:
            amount = amount - 10
            troco.append(10)
        if 10 > amount >= 5:
            amount = amount - 5
            troco.append(5)
        if 5 > amount >= 2:
            amount = amount - 2
            troco.append(2)
        if 2 > amount >= 1:
            amount = amount - 1
            troco.append(1)
            
    return troco
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:31:06 2023

@author: tiago
"""

import random

def cows_bulls(seed_value):
    random.seed(seed_value)
    correct = format(random.randint(0000,10000), '04d')
    
    print(correct)
    def check(guess):
        cows, bulls = 0, 0
        correc, guess = str(correct), str(guess)
        for i, digit in enumerate(correc):
            if digit == guess[i]:
                cows += 1
            if digit in guess:
                bulls += 1
        return (cows, bulls - cows)

    return check 

print(cows_bulls(510)(3834))
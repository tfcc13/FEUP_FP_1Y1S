#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:27:51 2022

@author: tiago
"""
from math import sqrt

def primes_range(start, stop):
    primes = get_primes()
    

    for _, prime in zip(range(stop+1), primes):
        if prime in range(start,stop+1):
            yield prime 

def get_primes():
    candidate = 2
    found = []
    while True:
        if all(candidate % prime != 0 for prime in found):
            yield candidate
            found.append(candidate)
        candidate += 1
        
print(list(primes_range(1, 10)))
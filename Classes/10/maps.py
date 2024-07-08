#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 10:47:48 2022

@author: tiago
"""

def celsius_to_fahrenheit(degrees):
    return degrees*9/5+32

temperatures_celsius = [18, 19, 21, 22, 24, 24, 22, 22]

results = []

for i in temperatures_celsius:
    f = celsius_to_fahrenheit(i)
    results.append(f)

print(results)

#using map

results = map(celsius_to_fahrenheit, temperatures_celsius)
print(list(results))

def is_even(x):
    
    return x%2 == 0

def impossible(x):
    return False

def universal(x):
    return True
even_numbers = filter(is_even, [1,2,3,4])
print(list(even_numbers))    
  

# Using lambdas

k = list(map(lambda x:x*2+1,[1,2,3]))
print(k)

# podia usar a conversao dos celsius para fharenheit sem precisar de definir uma funçaõ
#com os lambdas

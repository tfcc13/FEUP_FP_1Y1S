#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 10:57:41 2022

@author: tiago
"""

drinks = {"gin":2,"Super Bock":24,"guiness":6}

avail = drinks["Super Bock"]

print(drinks["Super Bock"])

drinks["Super Bock"] = avail -3 

drinks["Super Bock"] = drinks["Super Bock"] -3  

print(drinks)

for i in drinks:
    print(i)
    
for i in drinks.values():
    print(i)

for (k,v) in drinks.items():
    print(f"I have {k} of {v} to drink")

for i in drinks.items():
    print(i)

"""
alias = drinks
alias["guiness"] = 0 
print(drinks)
"""

alias2 = drinks.copy()

print(drinks == alias2)
print(drinks is alias2)

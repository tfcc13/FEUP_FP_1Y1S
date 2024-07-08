#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 18:46:55 2022

@author: tiago
"""



def is_prime(n):
    prime = True
    count = 0 
    for i in range(2,n+1):
        if  n % i == 0:
            count += 1
    if count > 1:
        prime = False
    return prime
        
lower = int(input())
upper = int(input())

prime_numbers = ""
        

for i in range(lower,upper+1):
    if is_prime(i) == True and i > 1:
        prime_numbers = prime_numbers + " " + str(i)

print(f"Prime numbers between {lower} and {upper} are:{prime_numbers}")
        
    
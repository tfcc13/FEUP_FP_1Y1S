#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 09:31:26 2022

@author: tiago
"""

def roman_to_integer(a_string):
    roman_to_decimal = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000,}
    subtract = {-2: ["IV", "IX"], -20:["XL","XC","XM","XD"], -200:["CD","CM"],}
    result = 0
    for i in a_string:
        result = result + roman_to_decimal[i]
        #print(result)
        
    for (key,value) in subtract.items():
        for i in value:
            if i in a_string:
                #print(i)
                result += key
                #print(result)
                

    return result

 	

print(roman_to_integer('LXXXIV'))
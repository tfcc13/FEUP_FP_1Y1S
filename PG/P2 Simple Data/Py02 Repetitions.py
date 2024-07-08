#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:50:13 2022

@author: tiago
"""

text = str(input())
num = int(input())
new = ""
for i in range(num):
    new = new + text 
    if i < num-1:
        new = new + "-"
    
    
print(new)


2

	
#ALTERNATIVAS

word = str(input())
print((word + '-')*(int(input())-1)+word) 

#ALTERNATIVAS 1

text= input()
num=int(input())
b= '-'
string= text+b
repeat= (string*(num-1))+text
print(repeat)

#ALTERNATIVAS 2

text = str(input())
num = int(input())
print(text + ("-" + text)*(num - 1))
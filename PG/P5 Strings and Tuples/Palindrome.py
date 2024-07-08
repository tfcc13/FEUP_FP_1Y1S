#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 12:00:50 2022

@author: tiago
"""

def palindrome_index(s):
    new = s
    
    if check(s) == True:
        return -1
    for i in range(1,len(s)+1):

        if check(new) != True:
            new = s[:i] +s[i+1:]
        elif check(new) == True and i != 0:
            return i-1
    return -1
    


            
    
def check(s):    
    

    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True



print(palindrome_index("abcejba"))
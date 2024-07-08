#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 08:40:39 2022

@author: tiago
"""

def rm_letter_rev(ch, s):
    result = ""
    ln = len(s)-1
    if ch in s:
        while ln >= 0:
            if ch == s[ln]:
                result = result + ""
            else:
                result = result + s[ln]
            ln -= 1    
    else:
        while ln>=0:
            result = result + s[ln]
            ln -=1
        
            
    return result

print(rm_letter("s", "A style guide is about consistency"))
                
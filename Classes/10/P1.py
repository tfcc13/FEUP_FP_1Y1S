#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 12:11:25 2022

@author: tiago
"""

def replace_rec(old_ch, new_ch, astring):
    
    if len(astring) == 0:
        return ""
    if astring[0] == old_ch:
        return  new_ch + replace_rec(old_ch, new_ch, astring[1:])
    return astring[0] +  replace_rec(old_ch, new_ch, astring[1:]) 
        
                
    
print(replace_rec("e", "_", "these are the best days"))
        
    
        
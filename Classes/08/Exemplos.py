#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:22:10 2022

@author: tiago
"""

def case_insensitive((item)):
    return item.lower()
"""
def anagram

    keys = []
    groups = []
    
    for s in sorted(alist, key=case_insensitive):
        
        s_key =  "".join(sorted(s.lower)).replace(" ", "")
        if s_keys not in keys:
            keys.append(s_key)
            groups.append(s)
        else:
            index = keys.index(s_key)
            groups [index].append(s)
            
        return groups
    
    keys = []
    groups = []
    
    for s in sorted(alist, key=case_insensitive):
        
        s_key =  "".join(sorted(s.lower)).replace(" ", "")
        if s_keys not in keys:
            keys.append(s_key)
            groups.append(s)
        else:
            index = keys.index(s_key)
            groups [index].append(s)
            
        return groups
 """
   
def anagram

    groups = {}
    
    for s in sorted(alist, key=case_insensitive):
        
        s_key =  "".join(sorted(s.lower)).replace(" ", "")
        if s_keys not in groups.keys:
            groups[s_key] = [s]
        else:
            groups[s_keys].appens(s)
            
   return list(groups.values())

print()
    

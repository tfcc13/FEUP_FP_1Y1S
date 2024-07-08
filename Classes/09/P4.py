#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 09:46:02 2022

@author: tiago
"""

def check(astring1, astring2):
    dict1 = {}
    
    for i,j in zip(astring1,astring2):
        if i in dict1 and dict1[i] != j:
            return False
        dict1[i] = j
    return dict1
    
def isomorphic(astring1,astring2):


    
    test1 = check(astring1, astring2)
    test2 = check(astring2, astring1)
    
    if test1 is False or test2 is False:
        
            return f"'{astring1}' and '{astring2}' are not isomorphic"
            
    lista = list(test1.items())
        
    return f"'{astring1}' and '{astring2}' are isomorphic because we can map: {lista}"
        


 	

print(isomorphic('ab', 'aa'))
print(isomorphic('paper', 'title'))
 	

print(isomorphic('foo', 'bar'))
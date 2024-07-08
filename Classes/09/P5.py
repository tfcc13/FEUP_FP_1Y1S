#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 20:03:19 2022

@author: tiago
"""

def check_results(bet, results):

    set1 =set()
    set2 = set()
    for n,i in enumerate(results):
        if i[2] > i[3]:
            set1.add((n,"1"))
        if i[2] < i[3]:
            set1.add((n,"2"))
        if i[2] == i[3]:
            set1.add((n,"X"))
        print(n,i[2],i[3])
            
    for n,k in enumerate(bet):
        print(n,k)
        set2.add((n,k))
    print(set1)
    print(set2)
    
    hits = len(set1&set2)
    
    
    return hits
        

print(check_results("XX121X221X122", [("Team A","Team B",0,0),
    ("Team C","Team D",2,1), ("Team E","Team F",0,4), 
    ("Team G","Team H",1,1), ("Team I","Team J",2,2), 
    ("Team K","Team L",2,0), ("Team M","Team N",1,0), 
    ("Team O","Team P",0,1), ("Team Q","Team R",0,0), 
    ("Team S","Team T",3,1), ("Team U","Team V",2,3), 
    ("Team X","Team Z",2,2), ("Team W","Team Y",1,5)]))
    
            
            
        
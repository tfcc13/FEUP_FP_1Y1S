#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 14:04:36 2022

@author: tiago
"""

import math
def tfidf(documents):
    doclist =[]
    dicdoc = {}
    n = len(documents)
    
    for j,i in enumerate(documents):
        doclist.append(i.split())
        doclist[j] = [x.lower() for x in doclist[j]]
    
        for word in doclist[j]:
            dicdoc[word] = [0] * n
    # print(doclist)
                     
   
        
    for i in range(n):
        for word in doclist[i]:
            dicdoc[word][i] += 1
            
                
        
    for j in dicdoc:
        num = n-dicdoc[j].count(0)
        idf =  math.log(n/num)
        for l in range(n):
            
            dicdoc[j][l] = round(dicdoc[j][l] * idf,3)
        
    return dicdoc

print(tfidf(['a', 'a one']))
print(tfidf(['To be or not to be', 'Impossible is a word to be found only in the dictionary of fools', 'There is nothing impossible to him who will try']))
        
        
        
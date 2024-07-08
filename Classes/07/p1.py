#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 08:34:49 2022

@author: tiago
"""

def mastermind(guesses, codes):
    correct = 0
    wrong = 0

    for i in range(len(guesses)):
        if guesses[i] == codes[i]:
            correct += 1
            guesses[i] = 1
            codes[i] = 0
    
    for i in range(len(guesses)):
        
        if guesses[i] in codes:
            wrong += 1
            codes[codes.index(guesses[i])] = 0
            guesses[i] = 1
    
    

    tupple =  (correct, wrong)
    
    return tupple  

"""def mastermind(guesses, codes):
    corpos = 0
    corcolor = 0
    for i in range (0, len(guesses)):
        if guess[i] == codes[i]:
            corpos +=1 
    for i in range (0, len(guesses)):
        if guess[i] != codes[i] and guess[i] in codes:
            corcolor += 1
    return (corpos, corcolor)
"""    




"""def mastermind(guesses, codes):
    soma1 = 0
    soma2 = 0
    for i in (guesses):
        count = 0
        for j in codes:
            if i == j and guesses[count]==codes[count]:
                soma1 += 1
                codes[count] = 0
                count += 1
                continue
            if i == j and guesses[count]!=codes[count]:
                soma2 += 1
                codes[count] = 1
                continue
            count += 1
            
        
    tuplo = (soma1,soma2)
    return tuplo
"""

"""
def mastermind(guesses, codes):
    soma1 = 0
    soma2 = 0
    for n,i in enumerate(guesses):
        if i == codes[n]:
            soma1 += 1
        if i in codes and i != codes[n]:
            soma2 += 1
    tuplo = (soma1,soma2)
    return tuplo
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:48:45 2022

@author: tiago
"""

def solver(a,b,c):
    if type(a) != str and type(b) != str and type(c) != str:
        testroots = b**2-4*a*c
    
        if testroots < 0:
            lista = []
            return lista
        else:
            raiz1 = (-b + testroots**0.5)/(2*a)
            raiz2 = (-b - testroots**0.5)/(2*a)
            if raiz1 != raiz2:
                lista = [raiz1,raiz2]
            else:
                lista = [raiz1]
            return sorted(lista)
    else:
        lista = []
        return lista
print(solver(1,0,0))
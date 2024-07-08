#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 16:06:45 2022

@author: tiago
"""

def fib(n):

    lista = [0,1]
    if n == 1:
        return [0]
    else:
        n_1 = 0
        n_2 =1
        for i in range(2,n):
            fibo = n_1 + n_2
            lista.append(fibo)
            n_1 = n_2
            n_2 = fibo
    return lista

print(fib(5))
            
            
        
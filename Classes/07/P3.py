#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:20:30 2022

@author: tiago
"""


def local_minima(alist):
    count = 0
    resultado = []
    teste = alist.copy()
    for i in range(len(alist)+1):
        if len(teste) < 3:
            break
        minilista = [teste[0],teste[1],teste[2]]
        minimo = min(minilista)
        for j in minilista:
            if minimo == j:
                count += 1
        if count == 1:
                resultado.append(minimo)
        del teste[0]
        count = 0
    return resultado

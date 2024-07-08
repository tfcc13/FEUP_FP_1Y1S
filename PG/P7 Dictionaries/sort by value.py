#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 15:32:23 2022

@author: tiago
"""

hexadict = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
 
def sort_by_value(dict1):
    lista = []
    result = []
    for i in dict1.items():
        x = hex_count(i[1])
        lista.append((i[0],x))
        
    lista.sort(key=lambda t: t[1])
    for i in lista:
        i = (i[0], dict1[i[0]])
        result.append(i)
    return result


def hex_count(hexa):
    count = 0
    soma = 0
    for i in hexa[-1:]:
        if i in hexadict.keys():
            soma += hexadict[i] * 16**count
        else:
            soma += int(i) * 16 ** count
        count += 1
    return soma

"""
def sort_by_value(adict):
    def get_hex(pair):
        return pair[1]
    return sorted(list(adict.items()), key=get_hex)
"""
        
print(sort_by_value({'Magenta': '#FF00FF', 'Red': '#FF0000', 'White': '#FFFFFF'}))
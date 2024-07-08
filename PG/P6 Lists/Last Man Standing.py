#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 15:42:24 2022

@author: tiago
"""

def last_man_standing(alist, step):
    
    while (len(alist)) > 1:
        if len(alist)>=step:
            alist.remove(alist[step-1])
            alist = alist[step-1:] + alist[:step-1]
        else:
            x = step%len(alist)
            alist.remove(alist[x-1])
            alist = alist[x-1:] + alist[:x-1]
    
    return alist[0]

"""
 2 cyclomatic complexity points


def last_man_standing(l,s):
    x=0
    while len(l)!=1:
       x=(x+s-1)%len(l)
       del l[x] 
    return l[0]


"""
print(last_man_standing([3, 4, 1, 6, 2, 5, 7], 3))
print(last_man_standing(['Andre', 'Rui', 'Silva', 'Madalena', 'Leonor', 'Francisco', 'Filomena'], 7))
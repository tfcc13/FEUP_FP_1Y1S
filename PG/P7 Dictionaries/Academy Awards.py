#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 13:18:24 2022

@author: tiago
"""

def academy_awards(alist):
    prizes = {}
    for i in alist:
       prizes[i[1]] = prizes.get(i[1], 0) +1
    
    return prizes

print(academy_awards([('Best Picture', 'Moonlight'), ('Best Director', 'La La Land'), ('Best Actor', 'Manchester by the Sea'), ('Best Actress', 'La La Land'), ('Best Supporting Actor', 'Moonlight'), ('Best Supporting Actress', 'Fences'), ('Best Original Screenplay', 'Manchester by the Sea'), ('Best Original Score', 'La La Land')]))
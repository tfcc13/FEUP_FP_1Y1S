#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:46:08 2022

@author: tiago
"""

def mask_data(data, n_characters, position):
    final = ""
    ln = len(data)
    dif = ln - n_characters
    if position == "begin":
        for i in data[n_characters::]:
            
            final = final + i
        return n_characters*"*"+ final
    elif position == "end":
        for i in data[:dif]:
            final = final +i
        return final + n_characters* "*"
    
 	

 	

 	

 	

print(mask_data("910432409", 4, "end"))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 08:55:53 2022

@author: tiago
"""

import string
def camel_case(phrase):
    
    result = phrase[0].lower()
    upper = False
    
    
    for i in phrase[1::]:
        if i.isupper() and upper == False:
            result = result + i.lower()
            upper = False
        elif i.isalpha() == False:
            result = result +""
            upper = True
        elif i.islower() == True and upper == True:
            result = result + i.upper()
            upper = False
        else:
            result = result + i
            upper = False

        
    return result

print(camel_case("What about Now?"))
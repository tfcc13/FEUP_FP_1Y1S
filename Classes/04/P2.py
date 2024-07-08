#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 09:32:35 2022

@author: tiago
"""

hours = int(input("Insert the hours."))

minutes = int(input("Insert the minutes."))

if hours >=0 and hours < 24 and minutes < 60 and minutes >= 0:
    if hours > 12:
        hours = hours % 12
        if minutes > 0:
            print(f"{hours}:{minutes:02d} pm")
        else:
            print(f"{hours} pm")
    elif hours < 12 and hours > 0:
        if minutes > 0:
            print(f"{hours}:{minutes:02d} am")
        else:
            print(f"{hours} am")
    elif hours == 12:
        if minutes > 0:
            print(f"{hours}:{minutes:02d} am")
        else:
            print(f"{hours} pm")
    elif hours == 0:
        hours = 12
        if minutes > 0:
            print(f"{hours}:{minutes:02d} am")
        else:
            print(f"{hours} am")
    
else:
    print("INVALID DATE FORMAT")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 14:11:35 2022

@author: tiago
"""

def classify(weight, height):
    
    bmi = weight/height**2
    
    if bmi < 17.5:
        return "underweight"
    elif 17.0 <= bmi < 18.5:
        return "mild_underweight"
    elif 18.5 <= bmi < 25:
        return"normal"
    elif 25 <= bmi < 30:
        return "overweight"
    else:
        return "obese"
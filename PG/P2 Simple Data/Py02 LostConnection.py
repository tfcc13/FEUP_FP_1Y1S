#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 10:38:52 2022

@author: tiago
"""

import math

def time_until_lost_connection(direction_A, direction_B):
    speed = 5/3.6
    dist = 35000
    
    dif_angle = abs((direction_A-direction_B)*math.pi/180)
    
    #a² = b² + c² - 2 * b * c * cos A
    #andam a mesma velocidade logo o triangulo formado tem 2 lados iguais
    time_min = math.sqrt((dist**2)/(2-2*math.cos(dif_angle)))/speed/60

    return round(time_min,3)

time_until_lost_connection(0, 90)
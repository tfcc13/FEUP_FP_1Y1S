#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 20:49:43 2022

@author: tiago
"""

distance = int(input())
litres_per_100_km = float(input())
fuel_price = float(input())

cost = distance/100*litres_per_100_km*fuel_price

print(round(cost,2))
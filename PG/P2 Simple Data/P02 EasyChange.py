#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 10:11:26 2022

@author: tiago
"""

price = int(input())
money = int(input())
bill_50 = 0
bill_20 = 0
bill_10 = 0
bill_5 = 0


while money > price:
    if money < price:
        print("Cheap ass motherfucker!")
    else:
        change = money - price
        if change >= 50:
            bill_50 += 1
            change = change - 50
            money = money - 50
        elif change >= 20 and change < 50:
            bill_20 += 1
            change = change -20
            money = money - 20
        elif change >= 10 and change < 20:
            bill_10 += 1
            change = change -10
            money = money - 10
        else:
            bill_5 += 1
            change = change -5
            money = money - 5
print(f"{bill_50} {bill_20} {bill_10} {bill_5}")
            
            
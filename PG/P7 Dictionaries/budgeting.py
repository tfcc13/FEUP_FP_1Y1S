#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 01:27:55 2022

@author: tiago
"""

def budgeting(budget, products, wishlist):

    dict1= {}
    while True:
        if check_cost(products, wishlist) > budget:
            mini = min(products.keys(), key=products.get)
            print(mini)
            if mini in wishlist.keys():
                wishlist[mini] = wishlist.get(mini) - 1
                if wishlist[mini] == 0:
                    wishlist.pop(mini)
            else:
                products.pop(mini)
        else:
            return wishlist
        
            
    return wishlist
            

def check_cost(products,wishlist):
    cost = 0
    for i in wishlist.items():
        cost += products.get(i[0])*i[1]
    print(cost)
        
    return cost
    
print(budgeting(1000, {'ps4': 350, 'smartphone': 400, 'jacket': 40, 'pc': 600, 'glasses': 75}, {'ps4': 1, 'smartphone': 1, 'pc': 1}))
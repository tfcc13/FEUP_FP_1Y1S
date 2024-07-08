#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:43:10 2022

@author: tiago
"""

def fight(heroes, villain):
    
    for hero in heroes:
        if hero["category"] == villain["category"]:
            if hero["health"] >= villain["health"]:
                hero["score"] = hero.get("score") +1
                name = hero["name"]
                score = hero["score"]
                return f"{name} defeated the villain and now has a score of {score}"
            else:
                villain["health"] = villain["health"] - hero.get("health")/2
                name = villain["name"]
                health = villain["health"]
                
    return f"{name} prevailed with {health:.1f}HP left"

""" def fight(heroes, villain):
    lista = list(filter(lambda x: x['category'] in villain['category'], heroes))
    for element in lista:
        if villain['health'] > element['health']:
            villain['health'] -= 0.5 * element['health']
            continue
        return element['name'] + ' defeated the villain and now has a score of ' + str(element['score'] + 1) 
    return villain['name'] + ' prevailed with ' + str(villain['health']) + 'HP left'
"""
                
                
            
     
                
                
    
            

    

    
print(fight([{'name': 'Genos', 'health': 3000, 'category': 'S', 'score': 0}, {'name': 'Blizzard of Hell', 'health': 1000, 'category': 'B', 'score': 0}, {'name': 'Saitama', 'health': 9001, 'category': 'C', 'score': 0}, {'name': 'King', 'health': 3750, 'category': 'S', 'score': 1}], {'name': 'Hero Killer', 'health': 4000, 'category': 'S'}))

print(fight([{'name': 'Superman', 'health': 6000, 'category': 'S', 'score': 3}, {'name': 'Blizzard of Hell', 'health': 2000, 'category': 'B', 'score': 7}, {'name': 'Saitama', 'health': 18002, 'category': 'C', 'score': -2}, {'name': 'Queen', 'health': 4000, 'category': 'S', 'score': 0}], {'name': 'Killer Hero', 'health': 8000, 'category': 'S'}))
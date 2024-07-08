#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:29:09 2022

@author: tiago
"""

a = float(input())
b = float(input())
c = float(input())

root1 = round((-b + (b**2-4*a*c)**0.5)/(2*a),2)
root2 = round((-b - (b**2-4*a*c)**0.5)/(2*a),2)

print("The solutions are %s and %s" % (root1, root2))

#Alternativa melhor 

 b, c = float(input()), float(input()), float(input())

sol1 = (-b + (b ** 2 - (4 * a * c)) ** 0.5) / (2 * a)

sol2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)


print(f"The solutions are {round(sol1, 2)} and {round(sol2, 2)}")
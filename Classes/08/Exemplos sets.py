#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:24:09 2022

@author: tiago
"""



aset = set()

cities =  {"Paris", "Madrid", "London", "Berlin", "Paris", "London"}

print(type(cities))

aset1  = set([0, "a", "b","c"])


# aicionar elementos ao set

aset1.add("d")

print(aset1)

print("b" in aset1)

# contar vampiros usando intersecção
people = {"Jay", "Idrish", "Archi"}

vampires = {"Karan", "Arjun"}

print(people & vampires) # "people & vampires" creates a set of the intersection

print(people.union(vampires)) # creates a set of the sum of the two sets 

# remover um item do set

N = {1,2,3,4,5,6}

N.discard(3)

print(N)


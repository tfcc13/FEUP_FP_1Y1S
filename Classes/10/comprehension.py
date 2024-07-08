#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 10:14:57 2022

@author: tiago
"""


import math
import itertools


squares = [x**2 for x in range(1,10)]

squares_even_number = [x**2 for x in range(1,10) if x%2 ==0 ]

print(squares_even_number)

#using a map

squares2 = list(map(lambda x:x**2, range(1,10)))

#using a map and filter

squares_even_numbers2 = list(map(lambda x:x**2, filter(lambda x:x%2==0, range(1,10))))

print(squares_even_numbers2)

#test if a number is prime

def is_prime(n):

    divs = [d for d in range(2,n) if n%d == 0]
    return n > 1 and len(divs)==0    

print(is_prime(1))

y = [p for p in range(1,100) if is_prime(p)]

print(y)


def primes_upto(n):
    return [p for p in range(2,10) if is_prime(p)]

print(primes_upto(10))

def pythogorean(n):
    """"Build a list of troiple x,y,z such that x**2+y**2 = z**2
    such that x,y,z <n"""
    return [(x,y,z) for x in range(1,n)
            for y in range(1,n)
            for z in range(1,n)
                if x**2 + y**2 == z**2]

print(pythogorean(30))

#similar to :
    
#for x in range(1,n):
    #for y in range(1,n):
        #for z in range(1,n):
            #if x ** 2+ y**2 == z**2:
                #print(x,y,z)
                
            
# construct the identity matrix

def identity_matrix(n):
    return[[int(row==col) for col in range(n)] for row in range(n)]



print(identity_matrix(3))


def pythogorean_gen(n):
    
    # generator only shhows a value when called by next(function)
    return ((x,y,x) for x in range(1,n) for y in range(1,n) for z in range(1,n) if x**2+y**2== z**2) # guarda o valor mas nao o mostra ao contrario do anterior

print(pythogorean_gen(10))




def gen_cosine(x):
    return ((-1)**n * x**(2*n) / math.factorial(2*n) for n in itertools.count(0))

def approx_cosine(x, n):
    g = gen_cosine(x)
    return sum(itertools.islice(g,n))
    

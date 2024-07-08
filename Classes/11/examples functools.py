#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:48:22 2022

@author: tiago
"""
import functools
"""def sum_squares(n):
    
    s = 0
    for i in range(1, n+1):
        s = s+i**2
    return s

def sum_cubes(n):
    
    s = 0
    
    for i in range(1, n+1):
        s = s + i **3
    return s

def summation(n, term):
    s = 0
    for i in range(1, n+1):
        s = s + term(i)
        
    return s

import functools

def example(x,y):
    return 3*x+y


print(list(map(lambda y: example(5,y), range(1,10))))

example5 = functools.partial(example, 5) # fix the first argument

print(list(map(example5, range(1,10))))


def another(x,y,z):
    return 3+x+y-z

another_3_5 = functools.partial(another,3,5)
"""
def example_curried(x):
    return lambda y: 3*x+y

def compose(f,g):
    def inner(x):
        return f(g(x))

f = lambda x:x+1
g = lambda x :3*x

fog = compose(f,g)

def into_words(str):
    
    return str.split()

remove_short = functools.partial(filter, lambda w: len(w)>=3)

def join_together(words):
    return " ".join(words)

combination = compose(compose(join_together, remove_short), into_words)

def combination(txt):
    return join_together(remove_short(into_words(txt)))


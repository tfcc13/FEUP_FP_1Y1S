#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 18:38:44 2022

@author: tiago
"""

def search_tree(key,tree):
    if key == None:
        return None
    if type(tree) is not tuple:
        return None
    
    (_key,value,left,right) = tree
    if _key == key:
        return (value, [_key])
    if key < tree[0]:
        r = search_tree(key, left)
    else:
        r = search_tree(key, right)
    
    
    if r == None:
        return None
    return(r[0], [_key] + r[1])

print(search_tree('apple', ('banana', 2, ('apple', 1, None, None), ('pear', 5, None, None))))
print(search_tree('pear', ('banana', 2, ('apple', 1, None, None), ('pear', 5, None, None))))

"""
def search_tree(key, tree):
    if key == None:
        return None
        
    if type(tree) is not tuple:
        return None
    
    if tree[0] == key:
        return (tree[1], [tree[0]])
    if key < tree[0]:
        return search_tree(key, tree[2])
    else:
        return search_tree(key, tree[3])
"""
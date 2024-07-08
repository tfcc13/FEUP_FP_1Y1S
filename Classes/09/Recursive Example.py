#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:05:57 2022

@author: tiago
"""

import os

def get_dirlist(path):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def get_dirtree(path, prefix=""):
    
    fullpath = os.path.join(prefix, path)
    
    if os.path.isdir(fullpath):
        subtrees = []
        names = get_dirlist(fullpath)
        for name in names:
           subtree = get_dirtree(name, fullpath)
           subtrees.append(subtree)
        return (path , subtrees)
    else:
        return path
    


#Recursive

def print_dirtree(tree, prefix = ""):
    if type(tree) is str:
        print(prefix + tree)
    else:
        (dirname,entries) = tree
        print(prefix + dirname)
        for subtree in entries:
            print_dirtree(subtree,prefix + "/")

print_dirtree(get_dirtree("home/tiago/Desktop/FEUP/FP/PG"))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 15:25:16 2022

@author: tiago
"""

def file_finder(dirs, file_name):
    if file_name == dirs:
        return dirs
    if type(dirs) == tuple:
        for i in dirs[1]:
            if type(i) is tuple:
                diret = file_finder(i,file_name)
                if diret:
                    return dirs[0] + "/" +diret
            elif i == file_name:
                return dirs[0] +"/" + file_name
                

print(file_finder(("home", [("Documents", [("FP", ["lists.txt", "recursion.pdf", "functions", "tmp.txt" ]), ("Python", ["hello_world.py", "readme.md" ])]), ("Downloads", [("Movies", [("TV Series", ["BreakingBad.mp4", "TheBigBangTheory.avi" ]), "1.avi", "22", "001.mp4"])]), "tmp.txt", "page.html"]), "Documents"))
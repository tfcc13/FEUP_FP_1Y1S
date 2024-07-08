#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 22:16:43 2022

@author: tiago
"""

def find_treasure(pos, steps):
    if steps == []:
        return pos
    elif steps[0] == "up":
        steps.remove("up")
        pos = find_treasure((pos[0], pos[1]+1), steps)
    elif steps[0] == "down":
        steps.remove("down")
        pos = find_treasure((pos[0], pos[1]-1), steps)
    elif steps[0] == "right":
        steps.remove("right")
        pos = find_treasure((pos[0]+1, pos[1]), steps)
    elif steps[0] == "left":
        steps.remove("left")
        pos = find_treasure((pos[0]-1, pos[1]), steps)
    return pos
print(find_treasure((0, 0), ['up', 'up', 'left', 'right', 'up', 'up']))
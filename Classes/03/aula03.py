#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:41:01 2022

@author: tiago
"""

import turtle

window = turtle.Screen()

alex = turtle.Turtle()

for i in range(4):
    alex.forward(50)
    alex.left(90)

window.mainloop()
turtle.bye()
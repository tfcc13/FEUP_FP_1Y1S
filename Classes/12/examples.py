#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:18:29 2022

@author: tiago
"""

import logging

logging.basicConfig(filename="example.log", level = logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info(
            "Running '{}' with arguments {}".format(func.__name__, args))
        return func(*args)
    return log_func

def add(x,y):
    return x+y

add_logger = logger(add)

print(add_logger(3,3))
print(add_logger(4,5))

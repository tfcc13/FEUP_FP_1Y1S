#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 13:35:09 2022

@author: tiago
"""

def remove_leading(ip):
    
    s = ip.split(".")
    sub_ip = []
    for i in s:
        k = str(int(i))
        sub_ip.append(k)
    
    return ".".join(sub_ip)
        
        

print(remove_leading('00.000.0'))
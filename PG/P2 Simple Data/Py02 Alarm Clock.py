#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 20:25:13 2022

@author: tiago
"""

hour = int(input("Insert the hour."))
minute = int(input("Insert the minutes."))

final_minute = minute+51
final_hour = hour+6

if final_minute >=  60:
    final_minute = final_minute % 60
    final_hour = final_hour+1
    if final_hour >= 23:
        final_hour =  final_hour % 24
else:
    if final_hour >= 23:
        final_hour = final_hour % 24
print("%02d:%02d" % (final_hour, final_minute))
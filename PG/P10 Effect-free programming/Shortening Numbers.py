#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:24:18 2023

@author: tiago
"""

# def shorten(suffixes, base):
#     def result(n):
#         try:
#             aux = int(n)
#         except:
#             return str(n)
        
#         if aux >= base:
#             res = ''
            
#             for i in range(len(suffixes)):
#                 aux = aux // base
#                 if aux >= 1:
#                     res = str(aux) + ' ' + suffixes[i + 1]
#                 else: 
#                     break
#             return res
#         return str(n) + ' ' + suffixes[0]
#     return result


def shorten(suffixes, base):
    
    def res(n):
        try:
             aux = int(n)
        except:
            return str(n)
        
        if aux >= base:
            res2 = ""
            
            for i in range(len(suffixes)):
                aux = aux // base
                if aux >= 1:
                    res2 = str(aux) + " " +suffixes[i+1]
                else:
                    break
            return res2
        return str(n) + " " + suffixes[0]
    return res

print(shorten( 	['', 'K', 'M'], 1000))
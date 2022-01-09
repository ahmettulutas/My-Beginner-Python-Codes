# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:29:12 2021

@author: Ahmet
"""
s = 'azcbobobegghakl'
numbob=0 
for i in range(0,len(s)): 
    if s[i:i+3]=="bob": 
        numbob+=1 
        print(numbob)
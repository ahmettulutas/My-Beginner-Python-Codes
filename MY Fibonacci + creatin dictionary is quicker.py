# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 12:49:45 2021

@author: Ahmet
"""

def fib(n):
    if n == 1:
        return(n)
    elif n == 2:
        return(n)
    else:
        return fib(n-1) + fib(n-2)

def efficientfib(n, d):
    if n in d:
        return d[n]
    else:
        ans = efficientfib(n-1, d) + efficientfib(n-2, d) 
        d[n] = ans
        return ans
dicto = {}
argTouse = 17
print("hold on")
print(fib(argTouse))
print("this will be quicker")
print(efficientfib(argTouse, dicto))
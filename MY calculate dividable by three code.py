# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:49:17 2021

@author: Ahmet
"""


standbymode = True

while standbymode is True:
 sum = 0
 number = input("write a number here")
 number = str(number)
 for i in number:
  i = int(i)
  sum = sum +i
 if sum % 3 == 0:
   print("your number is dividable".upper())  
 else:
   print("your number is not dividable".upper())
        


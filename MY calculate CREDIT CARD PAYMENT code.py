# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 17:38:49 2021

@author: Ahmet
"""

balance = 42
annualInterestRate = 0.2
monthlyInterestRate = 0.04
for i in range(12):
    monthlybalance = balance*monthlyInterestRate
    remainingbalance = balance - monthlybalance
    interest = ((annualInterestRate)/12)*(remainingbalance)
    remainingbalance = interest + remainingbalance
    balance = remainingbalance
    i +=1
    print(round(remainingbalance, 2))   
   

   
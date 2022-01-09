# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 14:19:37 2021

@author: Ahmet
"""
maxvalue = 100

minvalue = 0

ans = int((maxvalue + minvalue)/2)
print("I'm bored :O " + "Wanna play a game?" + " think of a number from 1 to 100 and\
 I will try to guess.")
print("Is this your number? = " + str(ans))
while True:
    guess = input("If this is a high guess press H, if low press L,\
 and if correct press C ")
    if guess == "h":
        maxvalue = ans
    elif guess == "l":
        minvalue = ans
    elif guess == "c":
        print("Game Over. :)")
        print("This is your number = " + str(ans))
        break
    else:
        print("Wrong letter. please type one of these = H, L or C".upper())
    ans = int((maxvalue + minvalue)/2)
    print("is this your number? = " + str(ans))

    
    


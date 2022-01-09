# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 13:26:16 2021

@author: Ahmet
"""
import random



def isWin (comp, user):
    if comp == "r" and user == "p":
       return True
    elif comp == "p" and user == "s":
       return True
    elif comp == "s" and user == "r":
       return True
    else:
       return False

def computersans (comp):
    if comp == "r":
      return "ROCK"
    if comp == "p":
      return "PAPER"
    else:
      return "SCISSORS"


ans = ("r", "p", "s")
while True:
      comp = random.choice(ans)
      print("Lets play rock paper scissors")
      user = input("press r for rock , p for paper, s for scissors = ")


      try:
          user in ans    
      except:
          raise ValueError
          print("please choose a valid letter. letters are >> p r s")
      if user == comp:
                print ("My choice is = " + comp +  " and your answer is = " + user)
                print ("Oh. Lucky you. Draw.. For now...")
            
      elif isWin (comp, user) == True:
                print (computersans(comp) + " " + "You won. great")


      else:
                print (computersans(comp) + " " + "I won hahaha")

          
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 00:58:00 2021

@author: Ahmet
"""

song = "It took multiple rounds of watching this video to get to a point where I think I understand what happened. I think that when Prof Grimsom tried to run most_common_word function the first time it ran the entire code (ahead of the lecture dialogue) including words_often & the print statement at the end (which set the 'best' variable to 5). It really made a confusing topic much more confusing."

def makingDict(freq):
    myDict = {}
    for word in (freq):
        if word in myDict:
            myDict[word] +=1
        else:
            myDict[word] = 1
    return(myDict)
print(makingDict(song)) # şarkı ya da senin örneğinde oldugu gibi song stringini dictionarye çevirirsin.
beatles = makingDict(song)
def mostcommonwords(frequent): # bu dictionary içindeki en çok tekrar eden kelimeyi bulmak için fonksiyon.
    values = frequent.values()
    best = max(values)
    words = []
    for k in(frequent):
        if frequent[k] == best:
            words.append(k)
    return(words, best)
print(mostcommonwords(beatles)) # en çok tekrarlanan kelimeleri bulursun.
(w, b) = mostcommonwords(beatles)
print(w)
print(b)
def words_often(freq, minTimes):
    result = []
    done = False
    while not done:
        temp = mostcommonwords(freq)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freq[w])
        else: 
            done = True
    return(result)

print(words_often(beatles, 40)) # 40ın üstünde tekrarlanan kelimeleri bulursun.
from random import *
class Player:
#פונקציה המאתחלת שחקן עם שם, כסף וכמות קלפים בחפיסה
    def __init__(self,name,money,maxcards=5):
        self.name= name
        self.money=int(money)
        self.playercards=[]
        self.maxcards=maxcards

#פונקציה המאתחלת חפיסה חדשה לשחקן
    def setHand(self, list):
        for i in range(0,self.maxcards,1):
            self.playercards.append(list.pop())

#פונקציה השולפת קלף רנדומלי מחפיסת השחקן
    def getCard(self):
        num=randint(len(self.playercards)+1)
        return self.playercards.pop(self.playercards[num])
#פונקציה המוסיפה קלף לחפיסת השחקן
    def addCard(self,card):
        if len(self.playercards)<5:
            self.playercards.append(card)
            print("the card added to player")
        else:
            print("the deck of player is full")
#פונקציה המקבלת סכום כסף ומורידה מהסכום של השחקן
    def reduceAmount(self, money):
        self.money-=money
#פונקציה המקבלת סכום כסף ומוסיפה לסכום של השחקן
    def addAmount(self,money):
        self.money+=money
#פונקציה המציגה את פרטי השחקן
    def __repr__(self):
       return (f'The player {self.name}, has {self.money} dollars and his cards are: {self.playercards}')




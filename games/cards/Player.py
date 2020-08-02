from random import *
from games.cards.Card import Card
class Player:
#פונקציה המאתחלת שחקן עם שם, כסף וכמות קלפים בחפיסה
    def __init__(self,name,money,maxcards=5):
        self.name= name
        self.money=int(money)
        self.playercards=[]
        self.maxcards=maxcards

#פונקציה המאתחלת חפיסה חדשה לשחקן
    def setHand(self, list):
        if len(list)<self.maxcards or len(list)>52:
            print("List Invalid")
        else:
            for i in range(0,self.maxcards,1):
                self.playercards.append(list.pop())

#פונקציה השולפת קלף רנדומלי מחפיסת השחקן
    def getCard(self):
        if(len(self.playercards)<1 or len(self.playercards)>5):
            print("Cards Pack Invalid")
        else:
            num=randint(0,len(self.playercards))
            return self.playercards.pop(num)

#פונקציה המוסיפה קלף לחפיסת השחקן
    def addCard(self,card):
        if type(card)==Card:
            print("This is a card")
            if card in self.playercards:
                print("Card is already exist in the deck of player")
            else:
                if len(self.playercards)<5 and len(self.playercards)>-1:
                    self.playercards.append(card)
                    print("the card added to player")
                else:
                    print("the deck of player is full")
        else:
            print("invalid Value - Not Card")
#פונקציה המקבלת סכום כסף ומורידה מהסכום של השחקן
    def reduceAmount(self, money):
        if  type(money) == int:
            if money > 0:
                self.money-=money
            else:
                print("Money to reduce can't be negative")
        else:
            print("Value Invalid")
#פונקציה המקבלת סכום כסף ומוסיפה לסכום של השחקן
    def addAmount(self,money):
        if type(money) == int:
            if money>0 :
                self.money+=money
            else:
                print("Money to add can't be negative")
        else:
            print("Value Invalid")
#פונקציה המציגה את פרטי השחקן
    def __repr__(self):
       return (f'The player {self.name}, has {self.money} dollars and his cards are: {self.playercards}')




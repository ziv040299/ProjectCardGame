from random import *
class Player:
    def __init__(self,name,money,maxcards=5):
        self.name= name
        self.money=int(money)
        self.playercards=[]
        self.maxcards=maxcards


    def setHand(self, list):
        for i in range(0,self.maxcards,1):
            self.playercards.append(list.pop())


    def getCard(self):
        num=randint(len(self.playercards)+1)
        return self.playercards.pop(self.playercards[num])

    def addCard(self,card):
        if len(self.playercards)<5:
            self.playercards.append(card)
            print("the card added to player")
        else:
            print("the deck of player is full")

    def reduceAmount(self, money):
        self.money-=money

    def addAmount(self,money):
        self.money+=money

    def __repr__(self):
       return (f'The player {self.name}, has {self.money} dollars and his cards are: {self.playercards}')




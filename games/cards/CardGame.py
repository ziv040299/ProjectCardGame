from games.cards.Player import Player
from games.cards.DeckOfCards import DeckOfCards
from random import *
class CardGame:
    def __init__(self,numofcards):
        self.listofcards=DeckOfCards().listcards
        self.numofcards=numofcards
        self.players=[]
        for i in range(0,4,1):
            player=Player(input("enter name of player"),input("enter amount of money"))
            self.players.append(player)



    def newGame(self):
        shuffle(self.listofcards)
        for i in range(0,len(self.players),1):
            for n in range(0,self.numofcards,1):
                self.players[i].addCard(self.listofcards.pop())


    def PayRound(self,round):
        sum=0
        for i in self.players:
            i.money-=100*round
            sum+=100*round
        return sum

    def CardsPerRound(self,pointer):
        return self.players[pointer].playercards.pop()



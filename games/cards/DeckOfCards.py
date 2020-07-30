from random import *
from games.cards.Card import Card
class DeckOfCards:
    def __init__(self):
        self.listcards=[]
        self.values=[2,3,4,5,6,7,8,9,10,11,12,13,14]
        self.suits=['Diamond','Spade', 'Heart', 'Club']
        for i in range(0,len(self.suits),1):
            for n in range(0,13,1):
                card1= Card(self.values[n],self.suits[i])
                self.listcards.append(card1)


    def shuffle(self):
        shuffle(self.listcards)

    def dealOne(self):
        self.listcards.pop()

    def newGame(self):
        shuffle(self.listcards)
        header=self.listcards[len(self.listcards)-1]

    def show(self):
        for i in self.listcards:
            print(i)




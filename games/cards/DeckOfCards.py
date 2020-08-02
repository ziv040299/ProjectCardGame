from random import *
from games.cards.Card import Card
class DeckOfCards:
#פונקציה המאתחלת משתנים של חבילת קלפים וכן בונה חבילה חדשה מלאה
    def __init__(self):
        self.listcards=[]
        self.values=[2,3,4,5,6,7,8,9,10,11,12,13,14]
        self.suits=['Diamond','Spade', 'Heart', 'Club']
        for i in range(0,len(self.suits),1):
            for n in range(0,13,1):
                card1= Card(self.values[n],self.suits[i])
                self.listcards.append(card1)

#פונקציה המערבבת חבילת קלפים
    def shuffle(self):
        shuffle(self.listcards)
#פונקציה המחזירה קלף מראש החפיסה
    def dealOne(self):
        if type(self.listcards[len(self.listcards)-1])!=Card:
            print("Invalid Value")
            return ("False")
        if len(self.listcards)==0 or len(self.listcards)>52:
            return "False"
        else:
            return self.listcards.pop()
#פונקציה המערבבת מחדש את החפיסה ומסמנת את ראש החפיסה
    def newGame(self):
        shuffle(self.listcards)
        header=self.listcards[len(self.listcards)-1]
#פונקציה המציגה את הקלפים בחפיסה
    def show(self):
        for i in self.listcards:
            print(i)




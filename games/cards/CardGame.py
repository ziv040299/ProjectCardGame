from games.cards.Player import Player
from games.cards.DeckOfCards import DeckOfCards
from random import *
class CardGame:
#פונקציית אתחול של משחק חדש
    def __init__(self,numofcards):
        self.listofcards=DeckOfCards().listcards
        self.numofcards=numofcards
        if type(numofcards)!=int:
            numofcards=5
            print("Invalid number of cards")
        if self.numofcards>5 or self.numofcards<0:
            self.numofcards=5
        self.players=[]
        for i in range(0,4,1):
            player=Player(input("enter name of player"),input("enter amount of money"))
            if player.money<5000 or player.money>10000:
                player.money=5000
            self.players.append(player)


#פונקציה שמתחילה משחק- מערבבת את חפיסת הקלפים ומחלקת קלפים לכל שחקן במשחק
    def newGame(self):
        shuffle(self.listofcards)
        for i in range(0,len(self.players),1):
            for n in range(0,self.numofcards,1):
                self.players[i].addCard(self.listofcards.pop())

#פונקציה שמקבלת מספר סיבוב ומחשבת ומחזירה את הפרס הכספי לאותו הסיבוב ע"י החסרה של כסף מכל אחד מהמשתתפים
    def PayRound(self,round):
        if type(round)!=int:
            return "False"
        elif round<0:
            return "False"
        else:
            sum=0
            for i in self.players:
                i.reduceAmount(100*round)
                sum+=100*round
        return sum
#פונקציה המקבלת מצביע ברשימת השחקנים במשחק, שולפת את הקלף האחרון בחפיסה שלו וכן מחזירה אותו
    def CardsPerRound(self,pointer):
        if type(pointer) != int:
            return "False"
        if pointer<0 :
            return "False"
        elif len(self.players[pointer].playercards) ==0:
            return "False"
        else:
            return self.players[pointer].playercards.pop()



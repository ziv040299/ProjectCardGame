from unittest import TestCase
from games.cards.Player import Player
from games.cards.Card import Card
from games.cards.DeckOfCards import DeckOfCards

class TestPlayer(TestCase):

    def test_set_hand(self): #checks the function not work with empty list
        player1 = Player("ziv", 5000, 4)
        list1=[]
        for i in range(3):
            card1=Card(4,"Heart")
            list1.append(card1)
        player1.setHand(list1)
        self.assertTrue(len(list1)==3)
    def test_set_hand2(self): #checks the function pull out from full list the maxcards number of cards
        player1 = Player("ziv", 5000, 4)
        list1 = []
        for i in range(52):
            card1=Card(4,"Heart")
            list1.append(card1)
        player1.setHand(list1)
        self.assertTrue(len(list1)==48)
    def test_set_hand3(self): #checks the function pull out from not full list the maxcards number of cards
        player1 = Player("ziv", 5000, 4)
        list1 = []
        for i in range(38):
            card1 = Card(4, "Heart")
            list1.append(card1)
        player1.setHand(list1)
        self.assertTrue(len(list1)==34)
    def test_set_hand4(self): #checks the function not pull out from over than full list the maxcards number of cards
        player1 = Player("ziv", 5000, 4)
        list1 = []
        for i in range(56):
            card1 = Card(4, "Heart")
            list1.append(card1)
        player1.setHand(list1)
        self.assertTrue(len(list1) == 56)
    def test_get_card(self): #checks that the function not work with empty list
        player1 = Player("ziv", 5000, 4)
        player1.playercards=[]
        player1.getCard()
        self.assertTrue(len(player1.playercards)==0)
    def test_get_card2(self): #checks that the function not work with more than 5 cards list
        player1 = Player("ziv", 5000, 4)
        player1.playercards = []
        for i in range(6):
            card1 = Card(4, "Heart")
            player1.playercards.append(card1)
        player1.getCard()
        self.assertTrue(len(player1.playercards) == 6)
    def test_get_card3(self):
        player1 = Player("ziv", 5000, 4)
        player1.playercards = []
        for i in range(4):
            card1 = Card(4, "Heart")
            player1.playercards.append(card1)
        player1.getCard()
        self.assertTrue(len(player1.playercards) == 3)
    #def test_get_card4(self):

    def test_add_card(self): #checks the function not works with full list of cards
        player1 = Player("ziv", 5000, 4)
        for i in range(5):
            card1 = Card(4, "Heart")
            player1.playercards.append(card1)
        player1.addCard(card1)
        self.assertTrue(len(player1.playercards)==5)

    def test_add_card2(self): #checks if function works with empty list and add card
        player1 = Player("ziv", 5000, 4)
        player1.playercards=[]
        card1 = Card(4, "Heart")
        player1.addCard(card1)
        self.assertTrue(len(player1.playercards) == 1)

    def test_add_card3(self): #checks if function works with valid list
        player1 = Player("ziv", 5000, 4)
        player1.playercards = []
        card1 = Card(4, "Heart")
        player1.playercards.append(card1)
        card2=Card(7,"Heart")
        player1.addCard(card2)
        self.assertTrue(len(player1.playercards) == 2)

    def test_add_card4(self): #check the function not put it an invalid value
        player1 = Player("ziv", 5000, 4)
        player1.addCard(5)
        self.assertTrue(len(player1.playercards)==0)

    def test_add_card5(self): #checks that function not insert the same card twice
        player1 = Player("ziv", 5000, 4)
        player1.playercards = []
        card1 = Card(4, "Heart")
        player1.playercards.append(card1)
        player1.addCard(card1)
        self.assertTrue(len(player1.playercards)==1)
    def test_reduce_amount(self):
        player1 = Player("ziv", 5000, 4)
        player1.reduceAmount(-300)
        self.assertTrue(player1.money==5000)

    def test_reduce_amount2(self):
        player1 = Player("ziv", 5000, 4)
        player1.reduceAmount("gdfga")
        self.assertTrue(player1.money == 5000)

    def test_reduce_amount3(self):
        player1 = Player("ziv", 5000, 4)
        player1.reduceAmount(300)
        self.assertTrue(player1.money == 4700)

    def test_add_amount(self):
        player1 = Player("ziv", 5000, 4)
        player1.addAmount(-300)
        self.assertTrue(player1.money == 5000)

    def test_add_amount2(self):
        player1 = Player("ziv", 5000, 4)
        player1.addAmount("fgafdg")
        self.assertTrue(player1.money == 5000)

    def test_add_amount3(self):
        player1 = Player("ziv", 5000, 4)
        player1.addAmount(300)
        self.assertTrue(player1.money == 5300)
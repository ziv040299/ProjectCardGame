from unittest import TestCase,mock
from unittest.mock import patch
from games.cards.DeckOfCards import DeckOfCards
from games.cards.Card import Card


class TestDeckOfCards(TestCase):

    def test_shuffle(self):
        deck1=DeckOfCards()
        with patch('games.cards.DeckOfCards.shuffle') as mock_shuffle:
            num=deck1.listcards[0]
            deck1.shuffle()
            self.assertTrue(deck1.listcards[0]!=num)



    def test_deal_one(self): #checks that function not works with empty list
        # with patch ('games.cards.DeckOfCards.DeckOfCards.dealOne') as mock_dealone:
        #     mock_dealone.return_value = 5
        #     deck1 = DeckOfCards()
        #     self.assertTrue(deck1.dealOne(),5)
        deck1=DeckOfCards()
        deck1.listcards=[]
        self.assertTrue(deck1.dealOne()!=True)

    def test_deal_one1(self): #checks that function not works with over than full list
        deck1 = DeckOfCards()
        deck1.listcards = []
        for i in range(53):
            card1=Card(i+1,"Heart")
            deck1.listcards.append(card1)
        self.assertTrue(deck1.dealOne() != True)

    def test_deal_one2(self): #checks that function not work with value that isn't type 'Card'
        deck1 = DeckOfCards()
        deck1.listcards = []
        for i in range(50):
            card1 = Card(i + 1, "Heart")
            deck1.listcards.append(card1)
        deck1.listcards.append(4)
        self.assertTrue(deck1.dealOne() != True)

    def test_deal_one3(self): #checks that the function works with valid list
        deck1 = DeckOfCards()
        deck1.listcards = []
        for i in range(50):
            card1 = Card(1, "Heart")
            deck1.listcards.append(card1)
        length=len(deck1.listcards)
        print(length)
        deck1.dealOne()
        print(len(deck1.listcards))
        self.assertTrue(len(deck1.listcards) == length-1)

    def test_new_game(self): #checks that the function suffle the valid list (52 values)
        deck1 = DeckOfCards()
        deck2=deck1.listcards.copy()
        deck1.newGame()
        break1=0
        for i in range(len(deck1.listcards)):
            if deck1.listcards[i]!=deck2[i]:
                break1+=1
                break
        self.assertTrue(break1==1)

    def test_new_game2(self): #checks that the function not works with unfull list
        deck1=DeckOfCards()
        deck1.listcards.pop()
        deck2=deck1.listcards.copy()
        deck1.newGame()
        self.assertTrue(deck1.listcards[0]==deck2[0])

    def test_show(self): #checks the function not work with invalid values
        deck1 = DeckOfCards()
        deck1.listcards=[]
        deck1.listcards.append(5)
        self.assertTrue(deck1.show()=="False")

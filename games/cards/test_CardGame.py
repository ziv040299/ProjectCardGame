from unittest import TestCase
from games.cards.Player import Player
from games.cards.DeckOfCards import DeckOfCards
from games.cards.CardGame import CardGame
from unittest import TestCase,mock
from unittest.mock import patch
from games.cards.Card import Card


class TestCardGame(TestCase):

    def test_new_game(self): #checks the function shuffle the list
        game1 = CardGame(5)
        game2 = game1.listofcards.copy()
        game1.newGame()
        break1 = 0
        for i in range(len(game1.listofcards)):
            if game1.listofcards[i] != game2[i]:
                break1 += 1
                break
        self.assertTrue(break1 == 1)

    def test_new_game2(self): #checks the function insert cards to player as the number of cards of the game
        game1 = CardGame(5)
        game1.newGame()
        self.assertTrue(len(game1.players[0].playercards)==game1.numofcards)



    def test_pay_round(self): #checks the function not works with negative round value
        game1=CardGame(5)
        self.assertTrue(game1.PayRound(-1)=="False")

    def test_pay_round2(self): #checks the function not works with invalid round value
        game1 = CardGame(5)
        self.assertTrue(game1.PayRound('gfdd') == "False")

    def test_pay_round3(self): #checks the function call right the stub function
        with patch('games.cards.Player.Player.reduceAmount') as mock_a:
            game1=CardGame(5)
            game1.PayRound(2)
            mock_a.assert_called_with(200)


    def test_cards_per_round(self): #checks the function not works with negative value of pointer
        game1 = CardGame(5)
        self.assertTrue(game1.CardsPerRound(-1)=="False")

    def test_cards_per_round2(self): #checks the function not works with invalid value of pointer
        game1 = CardGame(5)
        self.assertTrue(game1.CardsPerRound('fdg')=="False")

    def test_cards_per_round3(self):
        game1 = CardGame(5)
        game1.players[0].playercards=[]
        self.assertTrue(game1.CardsPerRound(3)=="False")

    def test_init_(self): #checks the function not starts a game with numofcards is'nt integer
        try:
            game=CardGame("ziv")
        except:
            pass
        else:
            self.fail()

    def test_init_2(self): #checks the function actually insert numofcards=5 if the user insert something else
       game=CardGame(6)
       self.assertTrue(game.numofcards==5)

    def test_init_3(self): #checks the function not insert empty name to player
        game = CardGame(5)
        self.assertTrue(game.players[0].name=="Player1")



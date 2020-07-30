from games.cards.Card import Card
from games.cards.Player import Player
from games.cards.DeckOfCards import DeckOfCards
from games.cards.CardGame import CardGame
from random import *
amount=randint(5000,10000)
print(amount)
game1=CardGame(5)
game1.newGame()
for i in game1.players:
    print(i)
for i in range(1,6,1):
    prize=game1.PayRound(i)
    list1=[]
    list2=[]
    list3=[]
    pointer=0
    for n in game1.players:
        nameofplayer=game1.players[pointer].name
        card=(game1.CardsPerRound(pointer))
        list1.append(card)
        list3.append(card)
        list2.append(nameofplayer)
        print(f'{nameofplayer} throw the card: {card}')
        pointer+=1
    maximumcardvalue=0
    maximumcardsuit=0
    for x in list1:
        if x.value>maximumcardvalue:
            maximumcardvalue=x.value
            maximumcardsuit=x.suitsnumbers[x.suit]
        elif x.value==maximumcardvalue:
            if x.suitsnumbers[x.suit]>maximumcardsuit:
                maximumcardsuit=x.suitsnumbers[x.suit]

    wincard=Card(maximumcardvalue,maximumcardsuit)
    print(f'The winner of the round is: {list2[list1.index(wincard)]}')
    for z in game1.players:
        if z.name==list2[list1.index(wincard)]:
            z.money+=prize
maximumwar=0
winner=''
for i in game1.players:
    if i.money>maximumwar:
        winner=i.name
print(f'The Big Winner Of The Game Is: {winner}!!!')









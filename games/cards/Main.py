from games.cards.Card import Card
from games.cards.Player import Player
from games.cards.DeckOfCards import DeckOfCards
from games.cards.CardGame import CardGame
from random import *
#קליטה של סכום כסף התחלתי לכל שחקן
amount=randint(5000,10000)
print(amount)
#קליטה של משחק חדש עם שליחה של כמות קלפים לכל שחקן
game1=CardGame(5)
game1.newGame()
#הדפסה של כל שחקן במשחק עם כמות הכסף שבידו והקלפים שהוא מחזיק
for i in game1.players:
    print(i)
#פתיחת משחק - 5 סיבובים
for i in range(1,6,1):
    prize=game1.PayRound(i)
    list1=[]
    list2=[]
    pointer=0
#כל שחקן במשחק זורק קלף מהחפיסה שלו
    for n in game1.players:
        nameofplayer=game1.players[pointer].name
        card=(game1.CardsPerRound(pointer))
        list1.append(card)
        list2.append(nameofplayer)
        print(f'{nameofplayer} throw the card: {card}')
        pointer+=1
#שמרנו את כל הקלפים שנזרקו בסיבוב בליסט1, ועכשיו בודקים איזה קלף הכי חזק ושומרים את הערכים שלו בשני משתנים וכמובן את השם של המנצח
    maximumcardvalue=0
    maximumcardsuit=0
    pointer2=0
    winneround=''
    for x in list1:
        if x.value>maximumcardvalue:
            maximumcardvalue=x.value
            maximumcardsuit=x.suit
            winneround=list2[pointer2]
        elif x.value==maximumcardvalue:
            if x.suitsnumbers[x.suit]>x.suitsnumbers[maximumcardsuit]:
                maximumcardsuit=x.suit
                winneround = list2[pointer2]
        pointer2+=1
#בונה משני המשתנים שמצאתי קלף חדש שהוא הקלף המנצח בסיבוב
    wincard=Card(maximumcardvalue,maximumcardsuit)
#הדפסה של המנצח בסיבוב + הקלף שזרק
    print(f'The winner of the round is: {winneround} with the card: {wincard}')
#חיפוש ברשימת השחקנים אחר השחקן שניצח בסיבוב והכנסת הפרס הכספי של הסיבוב לכמות הכסף שלו
    for z in game1.players:
        if z.name==winneround:
            z.addAmount(prize)
#הגדרת המנצח של המשחק ע"י שליפת השחקן בעל סכום הכסף המירבי (בסיום כל סיבובי המשחק)
maximumwar=0
winner=''
for i in game1.players:
    if i.money>maximumwar:
        winner=i.name
        maximumwar=i.money
#הדפסה של המנצח הגדול + כמות הכסף שבידו
print(f'The Big Winner Of The Game Is: {winner} With: {maximumwar} Dollars!!!')









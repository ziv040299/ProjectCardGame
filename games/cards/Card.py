class Card:
#פונקציה המאתחלת קלף חדש עם ערך וצורה
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit
#הגדרת מילון של מספרים וצורות על מנת שנוכל לעשות השוואה
        self.suitsnumbers = {'Diamond': 1, 'Spade': 2, 'Heart': 3, 'Club': 4}
#הצגה של הערך והצורה של הקלף
    def __repr__(self):
        return (f'value- {self.value}, suit- {self.suit}')

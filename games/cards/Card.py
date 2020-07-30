class Card:
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit
        self.suitsnumbers = {'Diamond': 1, 'Spade': 2, 'Heart': 3, 'Club': 4}
    def __repr__(self):
        return (f'value- {self.value}, suit- {self.suit}')

import random

class Card:
    def __init__(self, value, suit):
        key = {"2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, "10":9, "Jack":10, "Queen":11, "King":12, "Ace":13}
        self.value = str(value)
        self.suit = suit
        self.true_value = key[self.value]

class Deck:
    def __init__(self, shuffle=True):
        self.__values = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
        self.__suits = ["Clubs", "Spades", "Diamonds", "Hearts"]
        self.cards = [Card(j, i)  for i in self.__suits for j in self.__values]
        if shuffle:
            self.shuffle()

    def reset(self, shuffle=True):
        self.cards = [Card(j, i)  for i in self.__suits for j in self.__values]
        if shuffle:
            self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num=1):
        deal = self.cards[:num]
        self.cards = self.cards[num:]
        return deal

    def discard(self, num=1):
        self.cards = self.cards[num:]

class Coin:
    def __init__(self, toss=True):
        self.__values = ["Heads", "Tails"]
        self.value = "Heads"
        if toss:
            self.toss()

    def toss(self):
        self.value = random.choice(self.__values)

class Dice:
    def __init__(self, d_num=6, roll=True):
        self.sides=list(range(1, d_num+1))
        self.value=1
        if roll:
            self.roll()
    
    def roll(self):
        self.value=random.choice(self.sides)

if __name__=="__main__":
    pass

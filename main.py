#### Chris Padgett
#### Black Jack Game

import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
        
    def show(self):
        print(f'{self.val} of {self.suit}')


class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for s in ['Spades', 'Clubs', 'Hearts','Diamonds']:
            for v in range(1, 14):
                self.cards.append(Card(s,v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        # for i in range(len(self.cards)-1, 0, -1):
        for i in range(len(self.cards)):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def draw(self,deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()
    
    def handTotal(self):
        total = 0
        for card in self.hand:
            total += card.val
        return total
    
class Game:
    def __init__(self, player):
        self.deck = Deck()
        self.player = player
        self.dealer = Player('Dealer')
        self.startGame()
    
    def startGame(self):
        print('Starting game...\nDeck is being shuffled')
        self.deck.shuffle()
        self.dealCards()
        self.showDealerHand()
        self.showPlayerHand()
        self.askHitOrStay()
    
    def askHitOrStay(self):
        if input('Hit(1) or Stay(2)?') == '1':
            self.player.draw(self.deck)
            self.player.showHand()
            #If a Bust (Over 21)
            if self.player.handTotal() > 21:
                print('Bust!')
            if self.player.handTotal() <21:
                print('Yoooooo you didnt bust! Thats whats up!')
        else:
            print('Nah')
        
        
    def dealCards(self):
        print('Dealing Cards')
        self.player.draw(self.deck)
        self.dealer.draw(self.deck)
        self.player.draw(self.deck)
        self.dealer.draw(self.deck)
    
    def showDealerHand(self):
        print("Dealer's Hand")
        #Doesn't Show First Card [][6][1]
        for i in range(1,len(self.dealer.hand)):
            self.dealer.hand[i].show()
    
    def showPlayerHand(self):
        print(f"{self.player.name}'s Hand")
        self.player.showHand()





# deck = Deck()
chris = Player('Chris')

game = Game(chris)
# game.showDealerHand()
# game.showPlayerHand()

# chris = Player('Chris')




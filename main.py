#### Chris Padgett
#### Black Jack Game

import random
import time

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
        cardVals = [1,2,3,4,5,6,7,8,9,10,10,10,10]
        for s in ['Spades', 'Clubs', 'Hearts','Diamonds']:
            # for v in range(1, 14):
            for v in cardVals:
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
        # print(total)
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
        #handOnGoing
        self.handOnGoing = True
        self.player.stay = False
        self.dealer.stay = False
        while self.handOnGoing is True:
            if self.player.stay is False:
                self.playerChoice()
                self.checkPlayer()
            time.sleep(1)
            if self.dealer.stay is False:
                self.dealerChoice()
                self.checkDealer()
            if self.player.stay is True and self.dealer.stay is True:
                self.handOnGoing = False
        if self.handOnGoing is False:
            self.checkOutcome()


    def checkOutcome(self):
        if self.player.handTotal() <= 21 and self.player.handTotal() > self.dealer.handTotal():
            print(f'{self.player.name} Wins!')
        elif self.dealer.handTotal() <=21 and self.dealer.handTotal() > self.player.handTotal():
            print('Dealer Wins. :(')
        elif self.player.handTotal() > 21:
            print('Player Busted, You lose')
        elif self.dealer.handTotal() > 21:
            print('Dealer Busted, YOU WIN!')


    def playerChoice(self):
        hitStay = input('(H)it or (S)tay?')
        self.player.handTotal()
        if hitStay.lower() == 'h':
            self.player.draw(self.deck)
        elif hitStay.lower() == 's':
            self.player.stay = True
        #Check for input error
        else:
            print('Incorrect Input, Please type "H" or "S" ')
        self.player.showHand()
        self.player.handTotal()
    
    def checkPlayer(self):
        if self.player.handTotal() > 21:
            self.handOnGoing = False
        else:
            pass


    def dealerChoice(self):
        if self.dealer.handTotal() < 17:
            print('Dealer Draws')
            self.dealer.draw(self.deck)
            # self.showDealerHand()
            # if self.dealer.handTotal() > 21:
            #     print('Dealer Busted! You win.')
            #     self.dealerBust = True
        else:
            print(f'Dealer stays, Hand total:{self.dealer.handTotal()}')
            self.dealer.stay = True
        pass

    def checkDealer(self):
        if self.player.handTotal() > 21:
            self.handOnGoing = False
        else:
            pass

        # while self.playerBust is False and self.dealerBust is False and self.handOnGoing is True:
        #     self.playerChoice()
        #     time.sleep(2)
        #     if self.handOnGoing:
        #         self.dealerChoice()
        #     if self.dealerStay and self.playerStay:
        #         self.handOnGoing = False
        #         print("Both stayed. Who wins?")
        # if self.playerBust is True:
        #     print("Player Busted LAWL!")
        # elif self.dealerBust is True:
        #     print("Dealer Busted. LAWL!")


        # while self.handOnGoing:
        #     self.playerChoice()
        #     time.sleep(2)
        #     if self.handOnGoing:
        #         self.dealerChoice()
        #     if self.dealerStay and self.playerStay:
        #         self.handOnGoing = False
    #     self.checkWinner()
    
    # def checkWinner(self):

    #     pass



    # def dealerChoice(self):
    #     self.dealerStay = False
    #     # self.dealerBust = False
    #     if self.dealer.handTotal() < 17:
    #         print('Dealer Draws')
    #         self.dealer.draw(self.deck)
    #         self.showDealerHand()
    #         if self.dealer.handTotal() > 21:
    #             print('Dealer Busted! You win.')
    #             self.dealerBust = True
    #     else:
    #         print(f'Dealer stays, Hand total:{self.dealer.handTotal()}')
    #         self.dealerStay = True

    
    # def playerChoice(self):
    #     self.playerStay = False
    #     # self.playerBust = False
    #     if self.playerStay is False:  
    #         if input('Hit(1) or Stay(2)?') == '1':
    #             self.player.draw(self.deck)
    #             self.player.showHand()
    #             #If a Bust (Over 21)
    #             if self.player.handTotal() > 21:
    #                 self.playerBust = True
    #         else:
    #             print('Player Stays')
    #             self.player.handTotal()
    #             self.playerStay = True

        
        
    def dealCards(self):
        print('Dealing Cards\n')
        self.player.draw(self.deck)
        self.dealer.draw(self.deck)
        self.player.draw(self.deck)
        self.dealer.draw(self.deck)
    
    def showDealerHand(self):
        print("Dealer's Hand")
        #Doesn't Show First Card [][6][1]
        for i in range(1,len(self.dealer.hand)):
            self.dealer.hand[i].show()
        print("\n")
    
    def showPlayerHand(self):
        print(f"{self.player.name}'s Hand")
        self.player.showHand()
        print(f"Player Hand Total: {self.player.handTotal()}\n")







# deck = Deck()
chris = Player('Chris')

game = Game(chris)
# game.showDealerHand()
# game.showPlayerHand()

# chris = Player('Chris')




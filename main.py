#### Chris Padgett
#### Black Jack Game

import random
import time


#### Classes: Card, Deck, Player, Game
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
        self.player = Player(player)
        self.dealer = Player('Dealer')
        self.startGame()
    
    def startGame(self):
        
        #GAME ONGOING
        self.gameOngoing = True

        while self.gameOngoing is True:
            print('Starting game...\nDeck is being shuffled')
            self.deck.shuffle()
            #DEAL CARDS
            print('Dealing Cards\n')
            self.player.draw(self.deck)
            self.dealer.draw(self.deck)
            self.player.draw(self.deck)
            self.dealer.draw(self.deck)
            #SHOW EACH HAND
            self.showDealerHand()
            self.showPlayerHand()
            #START HAND
            self.playHand()

            userIn = input("Would you like to play again? (Y)es or (N)o\n")

            #PLAY AGAIN...RESET CARDS IN HAND
            if userIn.lower() == 'y':
                self.player.hand = []
                self.dealer.hand = []
                self.gameOngoing = True
            #DONT PLAY AGAIN
            elif userIn.lower() == 'n':
                self.gameOngoing = False

    def playHand(self):
        self.handOngoing = True
        self.player.stay = False
        self.dealer.stay = False
        while self.handOngoing is True:
            #PLAYER DOESNT STAY
            if self.player.stay is False:
                #Ask to Hit or Stay... Show hand, Check hand if > 21
                self.playerChoice()
                self.checkPlayer()
            time.sleep(1)
            #DEALER DOESNT STAY
            if self.dealer.stay is False and self.handOngoing is True:
                self.dealerChoice()
                self.checkDealer()
            #BOTH PLAYERS STAY
            if self.player.stay is True and self.dealer.stay is True:
                self.handOngoing = False
        #CHECK OUTCOME WHEN HAND IS OVER
        if self.handOngoing is False:
            self.checkOutcome()


    def checkOutcome(self):
        print(f'\n\nComparing Hand Totals...\nDealer hand total:{self.dealer.handTotal()}\nPlayer hand total:{self.player.handTotal()}')
            #IF (PLAYER > DEALER) & < 21
        if self.player.handTotal() <= 21 and self.player.handTotal() > self.dealer.handTotal():
            print(f'{self.player.name} Wins!')
            #IF (DEALER > PLAYER) & < 21
        elif self.dealer.handTotal() <=21 and self.dealer.handTotal() > self.player.handTotal():
            print('Dealer Wins. :(')
            #IF A PLAYER BUST
        elif self.player.handTotal() > 21:
            print('Player Busted, You lose')
            #IF A DEALER BUST
        elif self.dealer.handTotal() > 21:
            print('Dealer Busted, YOU WIN!')
            #TIE GAME
        elif self.dealer.handTotal() == self.player.handTotal():
            print('You tied, Dealer wins.')
        else:
            print("checkOutcome() 'else' statement")

    #PLAYER HIT OR STAY
    def playerChoice(self):
        #ASK INPUT FROM USER. Hit or Stay
        hitStay = input(f'Total: {self.player.handTotal()}... (H)it or (S)tay?')
        if hitStay.lower() == 'h':
            #HIT. Draw from Deck -> Display drawn card
            self.player.draw(self.deck)
            self.player.hand[-1].show()
        elif hitStay.lower() == 's':
            #STAY
            self.player.stay = True
        #Check for input error
        else:
            print('Incorrect Input, Please type "H" or "S" ')
            self.playerChoice()
    
    #CHECK IF PLAYER BUSTS
    def checkPlayer(self):
        if self.player.handTotal() > 21:
            print('BUST!')
            self.handOngoing = False
        else:
            self.showPlayerHand()
            pass

    #DEALER HIT OR STAY
    def dealerChoice(self):
        if self.dealer.handTotal() < 17:
            print('Dealer Draws')
            self.dealer.draw(self.deck)
        else:
            print(f'Dealer stays...')
            self.dealer.stay = True
        
    #CHECK IF DEALER BUSTS
    def checkDealer(self):
        if self.dealer.handTotal() > 21:
            print('BUST!')
            self.handOngoing = False
        else:
            self.showDealerHand()
            
    
    def showDealerHand(self):
        print("Dealer's Hand")
        #Doesn't Show First Card [X][6][1]
        print('XX of XXXXXXXX (Flipped card)')
        for i in range(1,len(self.dealer.hand)):
            self.dealer.hand[i].show()
        print("\n")
    
    def showPlayerHand(self):
        print(f"{self.player.name}'s Hand")
        self.player.showHand()
        print(f"Player Hand Total: {self.player.handTotal()}\n")



# chris = Player('Chris')

userIn = input('Enter your name!')

game = Game(userIn)





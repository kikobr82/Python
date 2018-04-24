import random
import time
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 11, 'King': 11, 'Ace': 1}

class Player:
    def __init__(self, player_name, bankroll):
        self.player_name = player_name
        self.bankroll = bankroll

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    deck = []
    def __init__(self):
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                Deck.deck.append(card)
    
    def shuffle(self):
        random.shuffle(Deck.deck)
    
    def __str__(self):
        deck_comp = ''  
        for card in self.deck:  
            deck_comp += '\n '+card.__str__()
        return 'The deck has:' + deck_comp

    def pop(self):
        return Deck.deck.pop(0)
        
class Hand:
    
    def __init__(self): 
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,Card): 
        self.cards.append(Card)

        print("Card {} of {} was dealt\n".format(Card.rank, Card.suit))

    def calculate_value(self, hand_name):
        self.value = 0
        aces = []
        print("{} have the following cards:".format(hand_name))
        for card in self.cards:
            if card.rank != "Ace":
                print("{} of {} ({})". format(card.rank, card.suit, values[card.rank]))
                self.value += values[card.rank]
            else:
                aces.append(card)
        for ace in aces:
            if self.value >= 11:
                print("{} of {} (1)". format(ace.rank, ace.suit))
                self.value += 1
            else:
                self.value += 11
                print("{} of {} (11)". format(ace.rank, ace.suit))
        print("Total value of {} cards: {}\n".format(hand_name, self.value))
        time.sleep(1)
        return self.value
    
    def __str__(self):
        deck_comp = ''  
        for card in self.cards:  
            deck_comp += '\n '+card.__str__()
        return 'The deck has:' + deck_comp
            


game_on = True
print("\n\nStarting the BlackJack game!")
name = input("Please, input your name to start: ")
player = Player(name, 300)
while game_on:
    game_deck = Deck()
    game_deck.shuffle()
    player_hand = Hand() 
    dealer_hand = Hand()
    print("Ok, {}, you now have a bankroll of {}.".format(player.player_name, player.bankroll))
    bet_size=0
    while bet_size == 0 or bet_size > player.bankroll:
        bet_size = int(input("Please, inform the value of the bet: "))

    player_hand.add_card(game_deck.pop())
    player_hand.add_card(game_deck.pop())
    player_hand.calculate_value(player.player_name)

    dealer_hand.add_card(game_deck.pop())
    dealer_hand.calculate_value("Dealer")

    if player_hand.value <= 21:
        hit_or_run = input("\nYou want another card? Y/N")
        hit_or_run = hit_or_run.upper()
        while hit_or_run != "N":
                player_hand.add_card(game_deck.pop())
                player_hand.calculate_value(player.player_name)
                if player_hand.value > 21:
                    break
                hit_or_run = input("\nYou want another card? Y/N")
                hit_or_run = hit_or_run.upper()
        if player_hand.value <= 21:
            dealer_hand.calculate_value("Dealer")
            while dealer_hand.value < 21 and dealer_hand.value < player_hand.value:
                print("Dealing another card...\n")
                dealer_hand.add_card(game_deck.pop())
                dealer_hand.calculate_value("Dealer")

    if player_hand.value > 21:
        print("{} has gone over 21 and lost!".format(player.player_name))
        player.bankroll -= bet_size
    if player_hand.value <= 21 and dealer_hand.value > 21:
        print("{} won with {} against {} of the Dealer".format(player.player_name, player_hand.value, dealer_hand.value))
        player.bankroll += bet_size
    elif player_hand.value == dealer_hand.value:
        print("{} and Delaer tied with {}".format(player.player_name, player_hand.value))
    elif player_hand.value <= 21 and dealer_hand.value <= 21:
        print("{} lost with {} against {} of the Dealer".format(player.player_name, player_hand.value, dealer_hand.value))
        player.bankroll -= bet_size    
    
    
    check_continue = input("\nYou want to play again? Y/N: ")
    check_continue = check_continue.upper()
    if check_continue == "N":
        print("\n\n{} ended the game with a {} bankroll".format(player.player_name, player.bankroll))
        break
    
    if player.bankroll <= 0:
        print("\n\nYou no longer have a bankroll! Game over!")
        break





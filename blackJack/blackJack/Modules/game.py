import random
from . import deck

cardValues = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 2, 'Queen': 3, 'King': 4, 'Ace': 11}

def calculateHandValue(hand):
    value = sum(hand)
    if 11 in hand and value > 21:
        hand.remove(11)
        hand.append(1)
    return value


deck = [(rank, suit) for suit in deck.suits for rank in deck.ranks]
random.shuffle(deck)

playerHand = []
dealer_hand = []

playerHand.append(deck.pop())
dealer_hand.append(deck.pop())
playerHand.append(deck.pop())
dealer_hand.append(deck.pop())

def startGame():


    while True:
        print("\nYour hand:")
        for card in playerHand:
            print(f"{card[0]} of {card[1]}")
        
        playerValue = calculateHandValue([cardValues[card[0]] for card in playerHand])
        print(f"Your hand value: {playerValue}")
        
        if playerValue == 21:
            print("Blackjack! You win!")
            break
        elif playerValue > 21:
            print("Bust! You lose.")
            break
        
        action = input("Do you want to hit or stand? (Hit/Stand): ").lower()
        
        if action == "h":
            playerHand.append(deck.pop())
        else:
            while calculateHandValue([cardValues[card[0]] for card in dealer_hand]) < 17:
                dealer_hand.append(deck.pop())
            
            print("\nDealer's hand:")
            for card in dealer_hand:
                print(f"{card[0]} of {card[1]}")
            
            dealer_value = calculateHandValue([cardValues[card[0]] for card in dealer_hand])
            print(f"Dealer's hand value: {dealer_value}")
            
            if dealer_value > 21:
                print("Dealer busts! You win!")
            elif dealer_value > playerValue:
                print("You lose.")
            elif dealer_value < playerValue:
                print("You win!")
            else:
                print("It's a tie!")
            
            break
    
        if len(deck) < 4:
            print("Not enough cards in the deck. The game is over.")
            break
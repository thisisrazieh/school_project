
import random;
SUITS = ['clubs' , 'diamonds' , 'Heart' , 'Spades'];
RANKS = ['2', '3', '5' ,'6', '7','8','9','10','jack','Queen','king','ace']


deck =[]
for rank in RANKS :
    for suit in SUITS:
        card= rank+ ' of '+suit
        deck+=[card]


n= len(deck)
for i in range(n):
    r = random. randrange(0 , i+1)
    temp =deck[r]
    deck[r]=deck[i]
    deck[i]  = temp
print (deck)
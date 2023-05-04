def hand_value(hand):
  total = 0
  for card in hand:
    total += card[2]
  return total

def card_string(card):
  article = "a "
  if card[0] in [8, "Ace"]: article = "an "
  return article + str(card[0]) + " of " + card[1]

hand = [ ("Jack", "Clubs", 10), ("7", "Hearts", 7), ("Ace", "Spades", 11) ]

print card_string(hand[0]), "has value", hand[0][2]
print card_string(hand[2]), "has value", hand[2][2]

print "Hand has value", hand_value(hand)
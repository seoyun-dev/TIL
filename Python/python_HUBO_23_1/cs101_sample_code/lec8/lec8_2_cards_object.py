class Card(object):
  """A Blackjack card."""
  pass

def card_string(card):
  article = "a "
  if card.face in [8, "Ace"]: article = "an "
  return article + str(card.face) + " of " + card.suit

def hand_value(hand):
  total = 0
  for card in hand:
    total += card.value
  return total

card1 = Card()
card1.face = "Ace"
card1.suit = "Spades"
card1.value = 11

card2 = Card()
card2.face = "Jack"
card2.suit = "Clubs"
card2.value = 10

card3 = Card()
card3.face = "7"
card3.suit = "Hearts"
card3.value = 7

hand = [ card1, card2, card3 ]

print card_string(card1), "has value", card1.value
print card_string(card2), "has value", card2.value

print "Hand has value", hand_value(hand)
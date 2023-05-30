import random




### (TASK1) 1~10,"Jack","Queen","King","Ace"를 하나의 리스트 (FACES) 로 만드시오
FACES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
SUITS = [ "Clubs", "Diamonds", "Hearts", "Spades" ]







### (TASK2) :Card 클래스를 생성하시오 (생성자 부분을 작성하시오) (Card object가 그 속성으로 face(2~A)와 suit(문양)를 갖도록)
### J,Q,K는 10으로 A는 11로 생각
### 예시 card1=Card("Jack","Diamonds") 일 때, cards1.face이 "Jack"이고 cards1.suit이 "Diamonds"가 되도록
class Card():
  def __init__(self, face, suit):
    assert(face in FACES and suit in SUITS)
    self.face = face
    self.suit = suit
    
  # 객체 정보 문자열 반환하는 내장 클래스 (print 역할)
  def __str__(self):
    article = "a "
    if self.face in [8, "Ace"]: article = "an "
    return article + str(self.face) + " of " + self.suit

  def value(self):
    if type(self.face) == int:
      return self.face
    if self.face == "Ace":
      return 11
    return 10






### (TASK3) Deck 클래스를 생성하시오 (생성자 부분을 작성하시오) 
### Deck 객체는 모든 카드를 포함하는 cards 리스트를 그 속성으로 (attribute) 가져야 함
class Deck():
  def __init__(self):
    self.cards = [Card(face, suit) for face in FACES for suit in SUITS]
    random.shuffle(self.cards)  # 덱을 생성하면서 섞는 함수

  def draw(self): # 덱에서 카드를 한장 뽑는 함수
    return self.cards.pop()







### (TASK4) hand 라는 카드들의 리스트에 대해서 그 모든 값을 합해서 계산하는 함수를 작성하시오
### 예시 
# card1=Card(3,"Diamonds")
# card2=Card(5,"Spades")
# card3=Card("ACE","Hearts")
# hand=[card1, card2, card3]
# sum=hand_value(hand) --> sum은 19가 되야함
def hand_value(hand):
  sum = 0
  for card in hand:
    if type(card.face) == int:
      sum += card.face
    else:
      sum += card.value()
  return sum








def ask_yesno(prompt):
  while True :
    user_input = input(prompt)
    if user_input == "y" :
      return True
    elif user_input == "n" :
      return False
    else :
      print("I beg your pardon!")
      
      
      
      
      
      
      
      
      
      

def blackjack():
  deck = Deck()
  dealer = []
  player = []
  
  
  
  ### (TASK5) palyer 리스트에 deck에서 뽑은 카드를 추가하시오. 추가하면서 어떤 카드가 뽑혔는지 프린트하시오
  ### 그다음에는 딜러 차례라서 dealer 리스트에 추가하시오. 다만 hidden 카드이므로 딜러가 히든 카드를 뽑았다고 프린트하시오
  ### 그 다음은 다시 플레이어 카드를 뽑고
  ### 그 다음은 딜러가 카드를 뽑고 
  ### 마지막으로 플레이어의 2장의 카드의 합을 프린트하시오
  player.append(deck.draw())
  print ("You are dealt", player[-1])
  dealer.append(deck.draw())
  print ("Dealer is dealt hidden card")
  player.append(deck.draw())
  print ("You are dealt", player[-1])
  dealer.append(deck.draw())
  print ("Dealer is dealt", dealer[-1])
  print ("Your total is", hand_value(player))


  while hand_value(player) < 21:
    if not ask_yesno("Would you like another card? (y/n) "):
      break
    player.append(deck.draw())
    print ("You are dealt", player[-1])
    print ("Your total is", hand_value(player))
  
  if hand_value(player) > 21:
    print ("You went over 21! You lost!")
    return -1
  print ("The dealer's hidden card was", dealer[0])
  
  
  
  while hand_value(dealer) < 17:
    dealer.append(deck.draw())
    print ("Dealer is dealt", dealer[-1])    
  
  
  
  player_total = hand_value(player)
  dealer_total = hand_value(dealer)
  print ("Your total is", player_total)
  print ("The dealer's total is", dealer_total)

  if dealer_total > 21:
    print ("The dealer went over 21! You win!")
    return 1

  if player_total > dealer_total:
    print ("You win!")
    return 1

  if player_total < dealer_total:
    print ("You lost!")
    return -1

  print ("You have a tie!")
  return 0











def game_loop():
  print("Welcome to Blackjack 101!")   
  while True:
    blackjack()    
    if not ask_yesno("Play another round? (y/n) "):
      break    

game_loop()

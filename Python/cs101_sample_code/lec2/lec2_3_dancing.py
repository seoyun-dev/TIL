import time
from cs1robots import*
load_world("./worlds/amazing1.wld")

hubo = Robot(beepers = 4)

def dance():
  for i in range(4):
    hubo.turn_left()
    time.sleep(0.1)

def move_or_turn():
  if hubo.front_is_clear():
    dance()
    hubo.move()
  else:
    hubo.turn_left()
    hubo.drop_beeper()

for i in range(20):
  move_or_turn()
  time.sleep(0.5)

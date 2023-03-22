import time
from cs1robots import*
load_world("./worlds/aroundtheworld.wld")

hubo = Robot(beepers = 1, avenue = 3, street = 1)
time.sleep(1.0)

def turn_right():
  for i in range(3):
    hubo.turn_left()

hubo.drop_beeper()
if not hubo.front_is_clear(): # --> while
  hubo.turn_left()
hubo.move()
time.sleep(0.5)

while not hubo.on_beeper():
  if hubo.right_is_clear():
    turn_right()
    hubo.move()
  elif hubo.front_is_clear():
    hubo.move()
  else:
    hubo.turn_left()
  time.sleep(0.5)

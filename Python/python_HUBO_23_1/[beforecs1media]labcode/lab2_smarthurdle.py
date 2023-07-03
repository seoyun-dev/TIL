
from cs1robots import *
import time
load_world("./worlds/hurdles1.wld")

hubo = Robot()
hubo.set_trace("blue")

def turn_right():
  for i in range(3):
    hubo.turn_left()

def jump_one_hurdle():
  hubo.turn_left()
  hubo.move()
  time.sleep(0.5)
  turn_right()
  hubo.move()
  turn_right()
  hubo.move()
  time.sleep(0.5)
  hubo.turn_left()

def move_or_jump():
  if hubo.front_is_clear(): 
    hubo.move()
    time.sleep(0.5)
  else:
    jump_one_hurdle()

while not hubo.on_beeper():
  move_or_jump()

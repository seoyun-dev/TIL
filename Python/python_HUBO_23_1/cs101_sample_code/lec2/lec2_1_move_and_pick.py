import time
from cs1robots import*
load_world("./worlds/beepers1.wld")

hubo = Robot(beepers = 1)

def move_and_pick():
  hubo.move()
  if hubo.on_beeper():
    hubo.pick_beeper()

for i in range(9):
  move_and_pick()
  time.sleep(0.5)


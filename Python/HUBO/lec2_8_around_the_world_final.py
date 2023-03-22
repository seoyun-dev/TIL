# This program lets the robot go around his world counter-
# clockwise, stopping when he returns to the starting point.
import time
from cs1robots import *
load_world("./worlds/amazing2.wld")
hubo = Robot(beepers = 1)

def turn_right():
  for i in range(3):
    hubo.turn_left()

def mark_starting_point_and_move():
  hubo.drop_beeper()
  while not hubo.front_is_clear():
    hubo.turn_left()
  hubo.move()

def follow_right_wall():
  if hubo.right_is_clear():
    # Keep to the right
    turn_right()
    hubo.move()
  elif hubo.front_is_clear():
    # move following the right wall
    hubo.move()
  else:
    # follow the wall
    hubo.turn_left()

# end of definitions, begin solution

mark_starting_point_and_move()

while not hubo.on_beeper():
  follow_right_wall()
  time.sleep(0.3)
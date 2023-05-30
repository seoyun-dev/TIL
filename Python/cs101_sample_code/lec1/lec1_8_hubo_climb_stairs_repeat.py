import time
from cs1robots import*

load_world("./worlds/newspaper.wld")

hubo = Robot(beepers = 1)

def turn_right():
  hubo.turn_left()
  hubo.turn_left()
  hubo.turn_left()

def turn_around():
  hubo.turn_left()
  hubo.turn_left()

def climb_up_four_stairs():
  for i in range(4):
    climb_up_one_stair()
    time.sleep(0.5)   

def climb_down_four_stairs():
  for i in range(4):
    climb_down_one_stair()
    time.sleep(0.5)   

def climb_up_one_stair():
  hubo.turn_left()
  hubo.move()
  turn_right()
  hubo.move()
  hubo.move()

def climb_down_one_stair():
  hubo.move()
  hubo.move()
  hubo.turn_left()
  hubo.move()
  turn_right()


climb_up_four_stairs()
hubo.drop_beeper()
turn_around()
climb_down_four_stairs()
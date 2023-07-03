import time
from cs1robots import *
load_world("./worlds/rain2.wld")
hubo = Robot(beepers = 10,avenue=3,street=6,orientation="E")

def turn_right():
  for i in range(3):
    hubo.turn_left()

def mark_starting_point_and_move():
  time.sleep(0.1)
  hubo.drop_beeper()
  turn_right()
  hubo.move()
 

def follow_right_wall():
  if hubo.right_is_clear():
    turn_right()
    hubo.move()
    if hubo.right_is_clear():
      hubo.turn_left()
      hubo.turn_left()
      hubo.move()
      turn_right()
      hubo.drop_beeper()
      hubo.move()  
  elif hubo.front_is_clear():
    hubo.move()
  else:
    hubo.turn_left()

mark_starting_point_and_move()
while not hubo.on_beeper():
  follow_right_wall()
  time.sleep(0.3)
hubo.pick_beeper()
hubo.turn_left()
 
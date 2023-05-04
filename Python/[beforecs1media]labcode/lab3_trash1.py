from cs1robots import *
load_world("./worlds/trash2.wld")

hubo = Robot()
hubo.set_trace("blue")

def turn_right():
  for _ in range(3):
    hubo.turn_left()

def move_straight():
  while hubo.front_is_clear():
    hubo.move()

def move_pick():
  while hubo.front_is_clear():
    if hubo.on_beeper():
      hubo.pick_beeper()
    else:
      hubo.move()
  while hubo.on_beeper():
      hubo.pick_beeper()

def comeback_to_start():
  hubo.turn_left()
  hubo.turn_left()
  move_straight()

def throw_and_comeback():
  turn_right()
  hubo.move()
  while hubo.carries_beepers():
    hubo.drop_beeper()
  hubo.turn_left()
  hubo.turn_left()
  hubo.move()
  hubo.turn_left()

def collect_and_throw_and_comeback():
  move_pick()
  comeback_to_start()
  throw_and_comeback()


collect_and_throw_and_comeback()

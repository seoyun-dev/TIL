from cs1robots import *
#create_world()
load_world("./worlds/harvest1.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.1)

def move_and_pick():
  hubo.move()
  if hubo.on_beeper():
    hubo.pick_beeper()

def turn_right():
  for i in range(3):
    hubo.turn_left()

def move_6():
  hubo.pick_beeper()
  for i in range(5):
    move_and_pick()

def zigzag():
  move_6()
  turn_right()
  hubo.move()
  turn_right()
  move_6()

def zig():
  zigzag()
  hubo.turn_left()
  hubo.move()
  hubo.turn_left()

hubo.move()
hubo.turn_left()
zig()
zig()
zigzag()


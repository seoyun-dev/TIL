#상수 c를 사용하여 smart zigzag를 해결



from cs1robots import *
load_world("./worlds/yardwork.wld")


hubo = Robot()
hubo.set_trace("blue")

def turn_right():
  for _ in range(3):
    hubo.turn_left()

def pick_and_move():
  while hubo.front_is_clear():
    while hubo.on_beeper():
      hubo.pick_beeper()
    hubo.move()
  


def zig():
  hubo.move()
  turn_right()
  pick_and_move()
  while hubo.on_beeper():
    hubo.pick_beeper()
  hubo.turn_left()

def zag():
  hubo.move()
  hubo.turn_left()
  pick_and_move()
  while hubo.on_beeper():
    hubo.pick_beeper()
  turn_right()

def go_to_start():
  pick_and_move()
  while hubo.on_beeper():
    hubo.pick_beeper()
  hubo.turn_left()
  
go_to_start()

c=0
while hubo.front_is_clear():
  if c==0:
    zag()
    c+=1
  else:
    zig()
    c-=1



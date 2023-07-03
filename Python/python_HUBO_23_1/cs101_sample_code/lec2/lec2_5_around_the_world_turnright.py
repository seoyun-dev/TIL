import time
from cs1robots import*
load_world("./worlds/amazing2.wld")
# 아래로 실행시 오류 lec2_6
#load_world("./worlds/amazing3.wld")  

hubo = Robot(beepers = 1)

def turn_right():
  for i in range(3):
    hubo.turn_left()

hubo.drop_beeper()
hubo.move()
while not hubo.on_beeper():
  if hubo.right_is_clear():
    turn_right()
    hubo.move()
  elif hubo.front_is_clear():
    hubo.move()
  else:
    hubo.turn_left()
  time.sleep(0.5)

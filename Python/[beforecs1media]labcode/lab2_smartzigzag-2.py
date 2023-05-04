from cs1robots import *
# street과 avnenue값을 입력받는 코드
#m=int(input("Number of streets-->"))
#n=int(input("Number of streets-->"))


#### break를 이용한 방법




create_world(streets=7, avenues=8)
hubo = Robot()
hubo.set_trace("blue")

def turn_right():
  for _ in range(3):
    hubo.turn_left()
  
def move_straight():
  while hubo.front_is_clear():
    hubo.move()

def zig():
  hubo.move()
  turn_right()
  move_straight()
  hubo.turn_left()

def zag():
  hubo.move()
  hubo.turn_left()
  move_straight()
  turn_right()


hubo.turn_left()
move_straight()
turn_right()

while True:
  zig()
  if not hubo.front_is_clear():
    break
  zag()
  if not hubo.front_is_clear():
    break
  
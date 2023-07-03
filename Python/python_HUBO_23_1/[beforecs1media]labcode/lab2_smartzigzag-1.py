from cs1robots import *
# street과 avnenue값을 입력받는 코드
#m=int(input("Number of streets-->"))
#n=int(input("Number of streets-->"))


#### 상수 c를 사용해서 번갈아 가면서 zig zag를 적용하는 방법




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
  hubo.turn_left()
  hubo.move()
  hubo.turn_left()
  move_straight()
  
def zag():
  turn_right()
  hubo.move()
  turn_right()
  move_straight()

hubo.turn_left()
move_straight()
zag()

c=0
while hubo.left_is_clear() and hubo.right_is_clear():
  if c==0:
    zig()
    c+=1
  else:
    zag()
    c-=1
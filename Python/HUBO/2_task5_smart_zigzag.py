from cs1robots import *

create_world(streets=9, avenues=10)

hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

# 휴보가 왼쪽으로 돌아 올라갔다가 내려오는 함수
def move_one_cycle():
    hubo.turn_left()
    while hubo.front_is_clear():
        hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    while hubo.front_is_clear():
        hubo.move()

for i in range(4):
    move_one_cycle()
    # 왼쪽으로 돌고 한칸 전진
    hubo.turn_left()
    hubo.move()
move_one_cycle()
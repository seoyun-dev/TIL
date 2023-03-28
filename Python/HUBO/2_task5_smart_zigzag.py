from cs1robots import *

create_world(streets=11, avenues=7)

hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

# 휴보가 왼쪽으로 돌아 올라가는 함수
def go_up_cycle():
    hubo.turn_left()
    while hubo.front_is_clear():
        hubo.move()
    
# 올라가서 오른쪽으로 돌아 한칸 이동후 오른쪽으로 돌아 내려오는 함수
def move_and_down_cycle():
    turn_right()
    hubo.move()
    turn_right()
    while hubo.front_is_clear():
        hubo.move()

# 사이클이 끝나고 왼쪽 돌아 한칸 이동후 올라가는 함수
def move_and_up_cycle():
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    while hubo.front_is_clear():
        hubo.move()

go_up_cycle()
move_and_down_cycle()
# 로봇 avenue(가로)가 짝수일 때, left 비었다면 -> 한 칸 이동 후 up
while hubo.left_is_clear():
    move_and_up_cycle()
    # 로봇 avenue가 홀수일 때, right 비었다면 -> 한 칸 이동 후 down
    if hubo.right_is_clear():
        move_and_down_cycle()
    # right가 벽일 때 종료
    else:
        break
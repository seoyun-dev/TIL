from cs1robots import *

create_world(streets=10, avenues=6)

hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

# 휴보가 왼쪽으로 돌아 올라가는 함수
def first_half_cycle():
    hubo.turn_left()
    while hubo.front_is_clear():
        hubo.move()
    
# 올라가서 오른쪽으로 돌아 한칸 이동후 내려오는 함수
def move_and_second_half_cycle():
    turn_right()
    hubo.move()
    turn_right()
    while hubo.front_is_clear():
        hubo.move()

# 사이클이 끝나고 다음 사이클로 이동
def cycle_to_cycle():
    hubo.turn_left()
    hubo.move()


while hubo.left_is_clear():
    first_half_cycle()
    # right가 벽이 아닐 때 half cycle 진행
    if hubo.right_is_clear():
        move_and_second_half_cycle()
        if hubo.left_is_clear():
            cycle_to_cycle()
    # right가 벽일 때 종료
    else:
        break



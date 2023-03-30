from cs1robots import *

load_world("./worlds/yardwork.wld")

hubo = Robot()
hubo.set_trace('red')

def turn_right():
    for _ in range(3):
        hubo.turn_left()

# 정면으로 이동하며 pick beepers
def move_straight_and_pick_beepers():
    # cycle 시작할 때 beeper 있으면 줍기
    while hubo.on_beeper():
        hubo.pick_beeper()
    # 이동하며 beeper 줍기
    while hubo.front_is_clear():
        hubo.move()
        while hubo.on_beeper():
            hubo.pick_beeper()

# 왼쪽으로 돌고 한 칸 이동 후 왼쪽으로 돌기
def first_half_to_second_half():
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()

# 오른쪽으로 돌고 한 칸 이동 후 오른쪽으로 돌기
def cycle_to_cycle():
    hubo.turn_right()
    hubo.move()
    hubo.turn_right()


while True:
    

# 집에 돌아와 drop beepers
while hubo.carries_beepers():
    hubo.drop_beeper()
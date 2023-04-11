# 최종 카운트가 76이면 최소

from cs1robots import *

load_world("./worlds/harvest2.wld")

hubo = Robot()
hubo.set_trace('red')

# 초기값 설정
count = 0

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def turn_around():
    for _ in range(2):
        hubo.turn_left()

def move_and_count():
    global count
    hubo.move()
    count += 1

def pick_and_move_right_and_up():
    # N 바라보는 기준
    turn_right()
    hubo.pick_beeper()
    move_and_count()
    hubo.turn_left()
    move_and_count()

def pick_and_move_right_and_down():
    hubo.pick_beeper()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()

def pick_and_move_down_and_right():
    hubo.pick_beeper()
    hubo.move()
    turn_right()
    hubo.move()

# Robot (1,7)로 이동
hubo.turn_left()
for _ in range(6):
    move_and_count()

# face=0: face North, face=1: face South
face = 0 
while hubo.on_beeper():
    if face == 0 and hubo.front_is_clear():
        pick_and_move_right_and_up()
    elif face == 0 and not hubo.front_is_clear():
        pick_and_move_right_and_down()
    elif face == 1:
        pick_and_move_down_and_right()

hubo.pick_beeper()      # (6,12) pick beeper








print("move count = ", count)
# 내 풀이 & 교수님 풀이 1
from cs1robots import *

load_world('worlds/yardwork.wld')
hubo = Robot()
hubo.set_trace('red')

def pick():
    while hubo.on_beeper():
        hubo.pick_beeper()

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def turn_around():
    for _ in range(2):
        hubo.turn_left()

def move_straight():
    while hubo.front_is_clear():
        hubo.move()

def move_and_pick():
    hubo.move()
    pick()

def move_and_pick_straight():
    pick()
    while hubo.front_is_clear():
        move_and_pick()

# startingpoint로 돌아오기
def back_to_start_point():
    while not hubo.facing_north():
        hubo.turn_left()
    hubo.turn_left()
    while hubo.front_is_clear():
        hubo.move()
    hubo.turn_left()
    while hubo.front_is_clear():
        hubo.move()
    hubo.turn_left()

def odd_cycle():
    hubo.move()
    turn_right()
    move_and_pick_straight()
    hubo.turn_left()

def even_cycle():
    hubo.move()
    hubo.turn_left()
    move_and_pick_straight()
    turn_right()


# sol1
c = 0
back_to_start_point()
pick()
move_and_pick_straight()
hubo.turn_left()
while hubo.front_is_clear():
    if c == 0:
        even_cycle()
        c += 1
    else:
        odd_cycle()
        c -= 1
back_to_start_point()

# sol2 - 교수님 풀이 2
back_to_start_point()
pick()
move_and_pick_straight()
hubo.turn_left()
while True:
    even_cycle()
    if not hubo.front_is_clear():
        break
    odd_cycle()
    if not hubo.front_is_clear():
        break
back_to_start_point()
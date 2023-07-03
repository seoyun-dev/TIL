# 내 풀이 & 교수님 풀이
from cs1robots import *

load_world('worlds/rain1.wld')
# load_world('worlds/rain2.wld')
hubo = Robot(beepers=10, street=6, avenue=2)
hubo.set_trace('blue')

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def turn_around():
    for _ in range(2):
        hubo.turn_left()

def mark_starting_point_and_move():
    hubo.move()
    hubo.drop_beeper()
    turn_right()
    hubo.move()

def judgment():
    if hubo.right_is_clear():
        turn_right()
        hubo.move()
        if hubo.right_is_clear():
            turn_around()
            hubo.move()
            turn_right()
            hubo.drop_beeper()
            hubo.move()
    elif hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()

mark_starting_point_and_move()
while not hubo.on_beeper():
    judgment()
hubo.pick_beeper()
turn_right()

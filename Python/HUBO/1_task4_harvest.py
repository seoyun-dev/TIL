# 내 풀이
from cs1robots import *

load_world('worlds/harvest1.wld')

hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def move_and_pick():
    hubo.move()
    hubo.pick_beeper()

def move_and_pick_5_time():
    for _ in range(5):
        move_and_pick()

def left_to_right_to_left():
    move_and_pick_5_time()
    hubo.turn_left()
    move_and_pick()
    hubo.turn_left()
    move_and_pick_5_time()

move_and_pick()
for _ in range(2):
    left_to_right_to_left()
    turn_right()
    move_and_pick()
    turn_right()
left_to_right_to_left()

# 교수님 풀이
from cs1robots import *
#create_world()
load_world("./worlds/harvest3.wld")

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.1)

def move_and_pick():
    hubo.move()
    if hubo.on_beeper():
        hubo.pick_beeper()

def turn_right():
    for i in range(3):
        hubo.turn_left()

def move_5():
    hubo.pick_beeper()
    for i in range(5):
        move_and_pick()

def zigzag():
    move_5()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    move_5()

def zig():
    zigzag()
    turn_right()
    hubo.move()
    turn_right()

hubo.move()
zig()
zig()
zigzag()

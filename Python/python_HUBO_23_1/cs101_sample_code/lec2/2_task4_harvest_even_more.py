# 내 풀이 & 교수님 풀이
from cs1robots import *

# load_world('worlds/harvest4.wld')
load_world('worlds/harvest1.wld')
# load_world('worlds/harvest3.wld')

hubo = Robot()
hubo.set_trace('blue')
hubo.set_pause(0.1)

def pick():
    while hubo.on_beeper():
        hubo.pick_beeper()

def move_and_pick():
    hubo.move()
    pick()

def turn_right():
    for i in range(3):
        hubo.turn_left()

def move_5():
    pick()
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
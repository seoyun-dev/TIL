from cs1robots import *

create_world()
hubo = Robot()
hubo.set_trace('red')
def turn_right():
    for _ in range(3):
        hubo.turn_left()

def move_9_steps():
    for _ in range(9):
        hubo.move()

def move_one_cycle():
    move_9_steps()
    turn_right()
    hubo.move()
    turn_right()
    move_9_steps()

def cycle_to_cycle():
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()

hubo.turn_left()
for _ in range(4):
    move_one_cycle()
    cycle_to_cycle()
move_one_cycle()


# 교수님 풀이
from cs1robots import *
create_world()
hubo=Robot()
hubo.set_trace("blue")

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def move_9():
    for _ in range(9):
        hubo.move()

def zigzag():
    move_9()
    turn_right()
    hubo.move()
    turn_right()
    move_9()

def zig():
    zigzag()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()

hubo.turn_left()
zig()
zig()
zig()
zig()
zigzag()
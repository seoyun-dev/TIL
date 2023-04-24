# 내 풀이
from cs1robots import *

load_world('worlds/harvest3.wld')

hubo = Robot(beepers=6)
hubo.set_trace('blue')

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def plant():
    if not hubo.on_beeper():
        hubo.drop_beeper()

def move_and_plant():
    hubo.move()
    plant()

def firstplant_and_move_and_plant_5():
    plant()
    for _ in range(5):
        move_and_plant()

def one_cycle():
    firstplant_and_move_and_plant_5()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    firstplant_and_move_and_plant_5()

hubo.move()
for _ in range(2):
    one_cycle()
    turn_right()
    hubo.move()
    turn_right()
one_cycle()

# 교수님 풀이
from cs1robots import *
import time
#create_world()
load_world("./worlds/harvest3.wld")

hubo = Robot(beepers=10)
hubo.set_trace("blue")
hubo.set_pause(0.1)

def plant():
    if not hubo.on_beeper():
        hubo.drop_beeper()

def move_and_plant():
    hubo.move()
    plant()

def turn_right():
    for i in range(3):
        hubo.turn_left()

def move_5():
    plant()
    for i in range(5):
        move_and_plant()

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

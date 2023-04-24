# 내 풀이
from cs1robots import *

load_world('worlds/newspaper.wld')

hubo = Robot(beepers=1)
hubo.set_trace('blue')

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def turn_around():
    for _ in range(2):
        hubo.turn_left()

def up_one_stair():
    hubo.turn_left()
    hubo.move()
    turn_right()
    for _ in range(2):
        hubo.move()

def down_one_stair():
    for _ in range(2):
        hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()

hubo.move()
for _ in range(4):
    up_one_stair()
hubo.drop_beeper()
turn_around()
for _ in range(4):
    down_one_stair()
hubo.move()

# 교수님 풀이
from cs1robots import*
import time
load_world("./worlds/newspaper.wld")

hubo = Robot(beepers = 1)
hubo.set_trace('blue')
def turn_right():
    for _ in range(3):
        hubo.turn_left()

def turn_around():
    for _ in range(2):
        hubo.turn_left()

def climb_up_four_stairs():
    for _ in range(4):
        climb_up_one_stair()
        time.sleep(0.5)   

def climb_down_four_stairs():
    for _ in range(4):
        climb_down_one_stair()
        time.sleep(0.5)   

def climb_up_one_stair():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.move()

def climb_down_one_stair():
    hubo.move()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()

hubo.move()
climb_up_four_stairs()
hubo.drop_beeper()
turn_around()
climb_down_four_stairs()
hubo.move()
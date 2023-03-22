from cs1robots import *

load_world("./worlds/newspaper.wld")

hubo = Robot(beepers=1)

def turn_right():
    for i in range(3):
        hubo.turn_left()

def turn_around():
    for i in range(2):
        hubo.turn_left()

def up_one_stair_and_move_two():
    hubo.turn_left()
    hubo.move()
    turn_right()
    for i in range(2):
        hubo.move()

def move_two_and_down_one_stair():
    for i in range(2):
        hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()

hubo.move()
for i in range(4):
    up_one_stair_and_move_two()
hubo.drop_beeper()
turn_around()
for i in range(4):
    move_two_and_down_one_stair()
hubo.move()
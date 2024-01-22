from cs1robots import *

# load_world('worlds/hurdles1.wld')
# load_world('worlds/hurdles2.wld')
# load_world('worlds/hurdles3.wld')
load_world('worlds/hurdles4.wld')

hubo = Robot()

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def jump_one_hurdle():
    hubo.turn_left()
    while not hubo.right_is_clear():
        hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    while hubo.front_is_clear():
        hubo.move()
    hubo.turn_left()

def move_or_jump():
    if hubo.front_is_clear():
        hubo.move()
    else:
        jump_one_hurdle()
    
while not hubo.on_beeper():
    move_or_jump()
from cs1robots import *

# load_world('worlds/rain1.wld')
load_world('worlds/rain2.wld')
hubo = Robot(beepers=10, street=6, avenue=2)

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def turn_around():
    for _ in range(2):
        hubo.turn_left()

def mark_starting_point_and_move():
    hubo.drop_beeper()
    turn_right()
    hubo.move()

def judgment():
    if hubo.left_is_clear():
        hubo.turn_left()
        hubo.move()
        if hubo.left_is_clear():
            hubo.drop_beeper()
            turn_around()
            hubo.move()
            hubo.turn_left()
            hubo.move()
    elif hubo.front_is_clear():
        hubo.move()
    else:
        turn_right()

mark_starting_point_and_move()
while not hubo.on_beeper():
    judgment()
hubo.pick_beeper()
hubo.turn_left()
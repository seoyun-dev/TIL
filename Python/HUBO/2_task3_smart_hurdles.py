from cs1robots import *

load_world("./worlds/hurdles3.wld")

hubo = Robot(beepers=6)
hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

#turn left 하여 허들 넘고 turn left 하는 함수
def jump_one_hurdle():
    hubo.turn_left()
    for i in range(2):
        hubo.move()
        turn_right()
    hubo.move()
    hubo.turn_left()

def jump_or_finish():
    while not hubo.on_beeper():
        if hubo.front_is_clear():
            hubo.move()
        if not hubo.on_beeper():
            jump_one_hurdle()

jump_or_finish()
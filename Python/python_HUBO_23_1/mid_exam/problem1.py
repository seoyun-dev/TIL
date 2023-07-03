from cs1robots import *

load_world('worlds/harvest4.wld')

hubo = Robot()

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def pick():
    while hubo.on_beeper():
        hubo.pick_beeper()

def move_straight():
    while hubo.front_is_clear():
        hubo.move()

def move_and_pick():
    hubo.move()
    pick()

def move_and_pick_straight():
    while hubo.front_is_clear():
        pick()
        move_and_pick()

def move_and_pick_odd_to_even_cycle():
    move_and_pick_straight()
    odd_to_even()
    move_and_pick_straight()
    even_to_odd()

def odd_to_even():
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()

def even_to_odd():
    turn_right()
    hubo.move()
    turn_right()

hubo.move()
for _ in range(3):
    move_and_pick_odd_to_even_cycle()
move_straight()
while hubo.carries_beepers():
    hubo.drop_beeper()
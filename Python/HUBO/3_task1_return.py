# 내 풀이
from cs1robots import *
create_world()

hubo = Robot(orientation='W', street=8, avenue=9)
hubo.set_trace('red')

def move_straight():
    while hubo.front_is_clear():
        hubo.move()


while not hubo.facing_north():
    hubo.turn_left()

hubo.turn_left()
move_straight()
hubo.turn_left()
move_straight()

# 교수님 풀이
from cs1robots import *
create_world(avenues=10, streets=7)

hubo = Robot(orientation ='W', avenue = 7, street = 5)
hubo.set_trace("blue")

def see_west():
    while not hubo.facing_north():
        hubo.turn_left()
    hubo.turn_left()

def move_straight():
    while hubo.front_is_clear():
        hubo.move()

def comeback_to_starting():
    see_west()
    move_straight()
    hubo.turn_left()
    move_straight()
    hubo.turn_left()

comeback_to_starting()
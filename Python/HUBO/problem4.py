from cs1robots import *

create_world()
hubo = Robot(orientation='W', avenue=7, street=10)

def count_avenue_or_street():
    count = 1
    while hubo.front_is_clear():
        hubo.move()
        count += 1
    return count

def get_hubo_orientation():
    count = 0
    while not hubo.facing_north():
        hubo.turn_left()
        count += 1
    if count == 0:
        orientation = 'N'
    elif count == 1:
        orientation = 'E'
    elif count == 2:
        orientation = 'S'
    else:
        orientation = 'W'
    return orientation

orientation = get_hubo_orientation()
hubo.turn_left()
avenue = count_avenue_or_street()
hubo.turn_left()
street = count_avenue_or_street()

print("(", orientation, ",", avenue, ",", street, ")")
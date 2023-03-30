from cs1robots import *

create_world()

hubo = Robot(orientation='S', avenue=7, street=5)
hubo.set_trace('red')

# 북쪽 세팅
while not hubo.facing_north():
    hubo.turn_left()

# 서쪽 세팅
hubo.turn_left()
# x -> 0
while hubo.front_is_clear():
    hubo.move()
# 남쪽 세팅
hubo.turn_left()
# y -> 0
while hubo.front_is_clear():
    hubo.move()
# 동쪽 세팅
hubo.turn_left()
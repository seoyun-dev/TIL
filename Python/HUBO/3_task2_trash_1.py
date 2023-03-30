from cs1robots import *

load_world("./worlds/trash1.wld")
# load_world("./worlds/trash2.wld")

hubo = Robot()
hubo.set_trace('red')

def turn_right():
    for _ in range(3):
        hubo.turn_left()

# start point - pick beeper
while hubo.on_beeper():
        hubo.pick_beeper()
# 끝까지 가며 pick beeper
while hubo.front_is_clear():
    hubo.move()
    while hubo.on_beeper():
        hubo.pick_beeper()

# 한 바퀴 돌기
hubo.turn_left()
hubo.turn_left()

# 다시 되돌아가기
while hubo.front_is_clear():
    hubo.move()
# 도착장소로 이동
turn_right()
hubo.move()
# drop beepers
while hubo.carries_beepers():
    hubo.drop_beeper()
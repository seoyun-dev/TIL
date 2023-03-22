from cs1robots import *

load_world("./worlds/hurdles1.wld")

hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

# 1칸이동 후 사이클을 돌고 turn left 하는 함수
def move_one_cycle():
    hubo.move()
    hubo.turn_left()
    for i in range(2):
        hubo.move()
        turn_right()
    hubo.move()
    hubo.turn_left()

for i in range(4):
    move_one_cycle()
hubo.move()
hubo.pick_beeper()
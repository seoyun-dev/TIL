from cs1robots import *

load_world("./worlds/harvest3.wld")

hubo = Robot(beepers=6)
hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

# 한 사이클 돌기 (왼->오->왼)
def pick_up_one_cycle():
    # 왼 -> 오
    for i in range(5):
        if not hubo.on_beeper():
            hubo.drop_beeper()
        hubo.move()
    if not hubo.on_beeper():
            hubo.drop_beeper()
    # half cycle 위해 이동 및 조정
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    # 오 -> 왼
    for i in range(5):
        if not hubo.on_beeper():
            hubo.drop_beeper()
        hubo.move()
    if not hubo.on_beeper():
            hubo.drop_beeper()

# 사이클에서 사이클로 이동할 때 조정
def after_cycle_to_start_cycle():
    turn_right()
    hubo.move()
    turn_right()

hubo.move()
for i in range(2):
    pick_up_one_cycle()
    after_cycle_to_start_cycle()
pick_up_one_cycle()
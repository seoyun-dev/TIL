from cs1robots import *

load_world("./worlds/harvest1.wld")

hubo = Robot()

def turn_right():
    for i in range(3):
        hubo.turn_left()

# 휴보가 한칸 이동 후 한 번 올라갔다 내려오고 원위치하는 함수
def move_one_cycle():
    hubo.move()
    hubo.turn_left()
    # up
    for i in range(5):
        hubo.pick_beeper()
        hubo.move()
    hubo.pick_beeper()
    # down 위해 이동 및 beeper 줍기
    turn_right()
    hubo.move()
    hubo.pick_beeper()
    turn_right()
    # down
    for i in range(5):
        hubo.move()
        hubo.pick_beeper()
    # 원위치
    hubo.turn_left()


for i in range(3):
    move_one_cycle()
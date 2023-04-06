from cs1robots import *

# load_world("./worlds/rain1.wld")
load_world("./worlds/rain2.wld")

hubo = Robot(beepers=10, avenue=3, street=6)
hubo.set_trace('red')

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def turn_around():
    for _ in range(2):
        hubo.turn_left()

def judgment():
    # 1. 오른쪽이 뚫렸을 때
    if hubo.right_is_clear():
        # 창이 열린건지 길인지 판단 위해 이동
        # 1-1. 오른쪽이 길일경우 move 후 끝
        turn_right()
        hubo.move()
        # 1-2. 오른쪽 창이 열림 -> 자리 돌아와 drop_beeper 하고 move
        if hubo.right_is_clear():
            turn_around()
            hubo.move()
            turn_right()
            hubo.drop_beeper()
            hubo.move()
    # 2. 정면이 벽일 때 -> 왼쪽으로 돌아 move
    elif not hubo.front_is_clear():
        hubo.turn_left()
        hubo.move()
    # 3. 정면이 벽이 아닐 때 -> move
    else:
        hubo.move()

# 시작점에 beeper 두기
hubo.drop_beeper()
turn_right()
hubo.move()
# 시작점(beeper)에 올때까지 이동
while not hubo.on_beeper():
    judgment()
# 시작점 도착시 beeper 줍기
hubo.pick_beeper()
turn_right()
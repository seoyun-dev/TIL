# 최종 카운트가 76이면 최소

from cs1robots import *

load_world("./worlds/harvest2.wld")

hubo = Robot()
hubo.set_trace('red')

# 초기값 설정
count = 0

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def turn_around():
    for _ in range(2):
        hubo.turn_left()

def move_and_count():
    global count
    hubo.move()
    count += 1

def pick_and_move_right_and_up():
    hubo.pick_beeper()
    turn_right()
    move_and_count()
    hubo.turn_left()
    move_and_count()

def judgment():
    if hubo.front_is_clear():
        pick_and_move_right_and_up()

# Robot (1,7)로 이동
hubo.turn_left()
for _ in range(6):
    move_and_count()

while hubo.on_beeper():
    judgment()

# 소용돌이 모양
# (1,7)에서 N 보고 있는 hubo
# 픽, 오른쪽, 위 반복 -> 언제까지? 벽에 부딪히기 전까지 혹은 비퍼 오른쪽 위에 비퍼가 없을때
# turn_right()
# 픽, 오른쪽, 위 반복

print("move count = ", count)
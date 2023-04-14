from cs1robots import *

load_world("./worlds/harvest2.wld")

hubo = Robot()
hubo.set_trace('red')

count = 0

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def turn_around():
    for _ in range(2):
        hubo.turn_left()

# 한 번 이동하면 count += 1 되는 함수
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

def one_cycle_pick_and_move(i):
    for _ in range(i):
        pick_and_move_right_and_up()
    turn_right()

# 휴보 (1, 7)로 이동
hubo.turn_left()
for _ in range(6):
    move_and_count()

for i in range(5):
    i = 5-i
    if i == 5:
        for _ in range(3):
            one_cycle_pick_and_move(i)
    else:
        for _ in range(2):
            one_cycle_pick_and_move(i)
# 마지막 (6,6) 비퍼 줍기
hubo.pick_beeper()

print("move count = ", count)
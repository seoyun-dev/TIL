# 내 풀이
from cs1robots import *

# load_world('worlds/trash1.wld')
load_world('worlds/trash2.wld')

hubo = Robot()

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def turn_around():
    for _ in range(2):
        hubo.turn_left()

# 비퍼 위에 있으면 다 줍는 함수
def pick():
    while hubo.on_beeper():
        hubo.pick_beeper()

# 가지고 있는 모든 비퍼를 떨어뜨리는 함수
def drop():
    while hubo.carries_beepers():
        hubo.drop_beeper()

# 한칸 이동 후 비퍼가 있는만큼 줍는 함수
def move_and_pick():
    hubo.move()
    pick()

# 정면으로 이동만 하는 함수
def move_straight():
    while hubo.front_is_clear():
        hubo.move()

# 정면이 clear하면 계속 이동하며 줍는 함수
def move_and_pick_straight():
    while hubo.front_is_clear():
        move_and_pick()

# drop 지점 이동 후 drop 후 돌아오기
def move_and_drop_and_comeback():
    turn_right()
    hubo.move()
    drop()
    turn_around()
    hubo.move()
    hubo.turn_left()

pick()
move_and_pick_straight()
turn_around()
move_straight()
move_and_drop_and_comeback()

# 교수님 풀이
from cs1robots import *
load_world("./worlds/trash2.wld")

hubo = Robot()
hubo.set_trace("blue")

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def move_straight():
    while hubo.front_is_clear():
        hubo.move()

def move_pick():
    while hubo.front_is_clear():
        if hubo.on_beeper():
            hubo.pick_beeper()
        else:
            hubo.move()
    while hubo.on_beeper():
        hubo.pick_beeper()

def comeback_to_start():
    hubo.turn_left()
    hubo.turn_left()
    move_straight()

def throw_and_comeback():
    turn_right()
    hubo.move()
    while hubo.carries_beepers():
        hubo.drop_beeper()
    hubo.turn_left()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()

def collect_and_throw_and_comeback():
    move_pick()
    comeback_to_start()
    throw_and_comeback()


collect_and_throw_and_comeback()

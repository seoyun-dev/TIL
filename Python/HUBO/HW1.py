# b. 각 함수마다 맨 위에 global count 작성해주기
# c. hubo.move()가 실행될 때 마다 count=count+1 혹은 count+=1을 통해 1씩 증가시켜주기

from cs1robots import *

load_world("./worlds/harvest2.wld")

hubo = Robot()
# hubo.set_trace('red')

# 초기값 설정
count = 0

def each_move_one_count():
    global count
    hubo.move()
    count += 1

def move_five():
    for _ in range(5):
        each_move_one_count()


# Robot (6,2)로 이동
move_five()
hubo.turn_left()
each_move_one_count()

while hubo.on_beeper() and hubo.front_is_clear():



print("move count = ", count)
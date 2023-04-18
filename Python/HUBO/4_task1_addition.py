from cs1robots import *

# load_world("./worlds/add1.wld")
load_world("./worlds/add2.wld")
# load_world("./worlds/add34.wld")

hubo = Robot(street=2, beepers=100)

def turn_right():
    for _ in range(3):
        hubo.turn_left()

def turn_around():
    for _ in range(2):
        hubo.turn_left()

def collect_number_at_street2():
    num_string = ""                                 # street 2에서 최종적으로 만든 숫자(String)
    while hubo.front_is_clear():
        hubo.move()
        num_string = num_string + pick_and_count()   # 최종 숫자 str = 지금까지 컬렉 str + 이번에 센 str
    return num_string

def collect_number_at_street1():
    num_string = ""                                # street 2에서 최종적으로 만든 숫자(String)
    while hubo.front_is_clear():
        num_string = pick_and_count() + num_string  # 최종 숫자 str = 이번에 센 str + 지금까지 컬렉 str
        hubo.move()
    return num_string

def pick_and_count():
    count = 0
    if hubo.on_beeper():
        while hubo.on_beeper():
            hubo.pick_beeper()
            count += 1
    return str(count)

def right_move_right():
    turn_right()
    hubo.move()
    turn_right()

def move_until_front_not_clear():
    while hubo.front_is_clear():
        hubo.move()

def drop_beepers_by_num(result_str):
    for i in result_str[::-1]:
        i = int(i)
        for i in range(i):
            hubo.drop_beeper()
        hubo.move()


first_num_string = ""
first_num_string += collect_number_at_street2()

right_move_right()

second_num_string = ""
second_num_string += collect_number_at_street1()

plus_result = str(int(first_num_string) + int(second_num_string))

turn_around()
move_until_front_not_clear()
turn_around()

drop_beepers_by_num(plus_result)
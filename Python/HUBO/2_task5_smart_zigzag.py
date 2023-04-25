# # 내 풀이
# from cs1robots import *

# create_world(streets=8, avenues=8)

# hubo = Robot()
# hubo.set_trace('blue')

# def turn_right():
#     for _ in range(3):
#         hubo.turn_left()

# # 0이면 짝수 avenue, 1이면 홀수 avenue
# hubo_avenue = 1

# hubo.turn_left()
# while True:
#     if hubo.front_is_clear():
#         hubo.move()
#     # 홀수 열 끝
#     elif hubo_avenue == 1:
#         if hubo.right_is_clear():
#             turn_right()
#             hubo.move()
#             turn_right()
#             hubo_avenue = 0
#         else:
#             break
#     # 짝수 열 끝
#     elif hubo_avenue == 0: 
#         if hubo.left_is_clear():
#             hubo.turn_left()
#             hubo.move()
#             hubo.turn_left()
#             hubo_avenue = 1
#         else:
#             break

# 교수님 풀이 1
# 상수 c를 사용해서 번갈아 가면서 zig zag를 적용하는 방법
# from cs1robots import *

# create_world(streets=8, avenues=10)

# hubo = Robot()
# hubo.set_trace('blue')

# def turn_right():
#     for _ in range(3):
#         hubo.turn_left()

# def move_straight():
#     while hubo.front_is_clear():
#         hubo.move()

# def left_move_and_up():
#     hubo.turn_left()
#     hubo.move()
#     hubo.turn_left()
#     move_straight()

# def right_move_and_down():
#     turn_right()
#     hubo.move()
#     turn_right()
#     move_straight()

# hubo.turn_left()
# move_straight()
# right_move_and_down()

# c = 0
# while hubo.left_is_clear() and hubo.right_is_clear():
#     if c==0:
#         left_move_and_up()
#         c = 1
#     else:
#         right_move_and_down()
#         c = 0

# # 교수님 풀이 2
# # break를 이용한 방법
# from cs1robots import *

# create_world(streets=7, avenues=7)
# hubo = Robot()
# hubo.set_trace("blue")

# def turn_right():
#     for _ in range(3):
#         hubo.turn_left()

# def move_straight():
#     while hubo.front_is_clear():
#         hubo.move()

# def zig():
#     hubo.move()
#     turn_right()
#     move_straight()
#     hubo.turn_left()

# def zag():
#     hubo.move()
#     hubo.turn_left()
#     move_straight()
#     turn_right()

# hubo.turn_left()
# move_straight()
# turn_right()
# while True:
#     zig()
#     if not hubo.front_is_clear():
#         turn_right()
#         break
#     zag()
#     if not hubo.front_is_clear():
#         hubo.turn_left()
#         break
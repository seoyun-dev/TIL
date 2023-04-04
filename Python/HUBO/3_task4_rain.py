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

# 시작점에 drop beeper 후 오른쪽으로 돌아 한 칸 이동
hubo.drop_beeper()
turn_right()
hubo.move()
while not hubo.on_beeper():
    while hubo.front_is_clear():
        hubo.move()
        # 판단
        if hubo.right_is_clear():
            turn_right()
            hubo.move()
            # 열린창
            if hubo.right_is_clear():
                turn_around()
                hubo.move()
                turn_right()
                hubo.drop_beeper()
            # 길
            else:
                turn_around()
                hubo.move()
                turn_around()
                break
    hubo.turn_left()


# while 정면이 clear하면(정면이 벽이 아니면)
    # 이동
    # if 오른쪽이 뚫렸으면
        # 창이 열린건지 길인지 판단
            # if 오른쪽 창이 열렸으면 drop_beeper
            # else if 오른쪽이 길이면 turn_right
                # turn_around 후 break (turn_left시 길을 볼 수 있또록)
# 정면이 벽이면 turn_left

# 휴보가 on_beeper(시작점)이면 멈춤

from cs1robots import*

load_world("./worlds/8queens.wld")

hubo = Robot(beepers = 1)

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

hubo.move()
#hubo.turn_left()
turn_right()
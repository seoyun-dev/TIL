from cs1robots import *

load_world("./worlds/add1.wld")
# load_world("./worlds/add2.wld")
# load_world("./worlds/add34.wld")

hubo = Robot(street=2)

def collect_number(count):
    num_string = ""
    while hubo.front_is_clear():
        hubo.move()
        if hubo.on_beeper():
            while not hubo.on_beeper():
                hubo.pick_beeper()
                count += 1
            num_string += str(count)
    return num_string


first_num_string = ""
first_num_string += collect_number(0)
print(first_num_string)
second_num_string = ""
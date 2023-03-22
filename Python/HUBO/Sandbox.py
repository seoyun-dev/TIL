from cs1robots import *

# Create a robot world
# load_world 와 같은 역할
create_world()
# Create a robot named 'hubo'
hubo = Robot(beepers=10)
# Turn on a trace for our robot with 'blue' color
hubo.set_trace('blue')

hubo.drop_beeper()
hubo.move()
hubo.turn_left()
hubo.move()
hubo.drop_beeper()
#hubo.pick_beeper()
import time
from cs1robots import *
load_world("../worlds/harvest2.wld")
hubo = Robot(orientation = 'N', avenue = 6, street = 2)

def turn_right(robot):
  for i in range(3):
    robot.turn_left()

def stairs(robot, n):
  for i in range(n):
    robot.pick_beeper()
    robot.move()
    time.sleep(0.2)
    turn_right(robot)
    robot.move()
    robot.turn_left()

def diamond(robot, n):
  for i in range(4):
    stairs(robot, n)
    robot.turn_left()
  
def harvest_all(robot):
  for i in range(3):
    n = 5 - 2 * i
    diamond(robot, n)
    robot.move()
    robot.move()
  
# harvest_all(hubo)


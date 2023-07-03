from cs1graphics import *
import math
import time

canvas = Canvas(400, 300)
canvas.setBackgroundColor("light blue")
canvas.setTitle("CS101 Drawing exercise")

def animate_sunrise(sun):
  w = canvas.getWidth()
  h = canvas.getHeight()
  r = sun.getRadius()
  x0 = w / 2.0
  y0 = h + r
  xradius = w / 2.0 - r
  yradius = h
  for angle in range(181):
    rad = (angle/180.0) * math.pi
    x = x0 - xradius * math.cos(rad)
    y = y0 - yradius * math.sin(rad)
    sun.moveTo(x, y)
  
ci = Circle(30)
canvas.add(ci)
ci.setFillColor("yellow")
ci.setBorderColor("red")
ci.setBorderWidth(1)
animate_sunrise(ci)

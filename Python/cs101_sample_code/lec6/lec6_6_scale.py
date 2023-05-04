from cs1graphics import *
import time

canvas = Canvas(400, 400)
canvas.setBackgroundColor("light blue")
canvas.setTitle("CS101 Drawing exercise")

r = Rectangle(150, 50)
sq = Square(100)
canvas.add(r)
canvas.add(sq)
sq.setFillColor("blue")
sq.setBorderColor("red")
sq.setBorderWidth(5)
sq.moveTo(200, 200)
r.setFillColor("green")
r.setBorderColor("black")
r.setBorderWidth(5)
r.moveTo(270, 150)

time.sleep(2)

sq.rotate(45)
sq.scale(1.5)
r.scale(0.5)

time.sleep(3)
for i in range(80):
 sq.scale(0.95)
 time.sleep(0.05)
canvas.remove(sq)

time.sleep(3)
r.scale(2.5)
for i in range(50):
 r.rotate(1*25)
 r.scale(0.95)
 time.sleep(0.05)
canvas.remove(r)
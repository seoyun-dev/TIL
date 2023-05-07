from cs1graphics import *

car = Layer()
tire1 = Circle(10, Point(-20,-10))
tire1.setFillColor('black')
car.add(tire1)
tire2 = Circle(10, Point(20,-10))
tire2.setFillColor('black')
car.add(tire2)
body = Rectangle(70, 30, Point(0, -25))
body.setFillColor('blue')
body.setDepth(60)
car.add(body)

canvas = Canvas(400, 300)
canvas.setBackgroundColor("light blue")
canvas.setTitle("CS101 Drawing exercise")
canvas.add(car)
car.moveTo(20, 250)

for i in range(50):
    car.move(2, 0)
for i in range(22):
    car.rotate(-1)
for i in range(50):
    car.move(2,-1)
for i in range(22): 
    car.rotate(1)
for i in range(50):
    car.move(2,0)
for i in range(10):
    car.scale(1.05)
car.flip(90)

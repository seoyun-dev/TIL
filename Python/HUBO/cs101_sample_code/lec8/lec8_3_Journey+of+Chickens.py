from cs1graphics import*

class Chicken(object):
  """Graphic representation of a chicken."""
  pass

def make_chicken(hen = False):
  layer = Layer()
  if hen:
    body = Ellipse(70,80)
    body.setFillColor("white")
  else:
    body = Ellipse(40,50)
    body.setFillColor("yellow")
  body.setBorderColor("yellow")
  body.setDepth(20)
  layer.add(body)
  
  if hen:
    wing = Ellipse(60,40)
    wing.setFillColor("white")
    wing.setBorderColor("yellow")  
    wing.move(15,20)
  else:
    wing = Ellipse(30,20)
    wing.setFillColor("yellow")
    wing.setBorderColor("orange")
    wing.move(10,15)
  wing.setDepth(19)
  layer.add(wing)
  
  if hen:
    eye = Circle(3)
    eye.setFillColor("black")
    eye.move(-15,-15)
  else:
    eye = Circle(2)
    eye.setFillColor("black")
    eye.move(-10,-0)
  eye.setDepth(18)
  layer.add(eye)
  
  if hen:
    beak = Square(8)
    beak.move(-36,0)
  else:
    beak = Square(4)
    beak.move(-22,0)
  beak.rotate(45)
  beak.setDepth(21)  
  beak.setFillColor("orange")
  beak.setBorderColor("orange")    
  layer.add(beak)
  
  if hen:
    head1 = Ellipse(5, 8)
    head1.setFillColor("red")
    head1.setBorderColor("red")
    head1.move(0, -42)
    head1.setDepth(22)
    layer.add(head1)
    
    head2 = Ellipse(5, 8)
    head2.setFillColor("red")
    head2.setBorderColor("red")
    head2.move(-6, -42)
    head2.setDepth(22)
    layer.add(head2)
  
  ch = Chicken()
  ch.layer = layer
  ch.body = body
  ch.wing = wing
  ch.eye = eye
  
  return ch


canvas = Canvas(1000,300)
canvas.setBackgroundColor("light blue")
canvas.setTitle("Jorney of Chickens")

ground = Rectangle(1000, 100)
ground.setFillColor("light green")
ground.move(500, 250)
canvas.add(ground)

sun = Circle(50)
sun.setFillColor("red")
sun.move(0,0)
canvas.add(sun)

chicken = make_chicken(True)
chick1 = make_chicken()
chick2 = make_chicken()
herd = Layer()


#Chicken
chicken.layer.move(600,200)
chick1.layer.move(720,210)
chick2.layer.move(800,210)

herd.add(chicken.layer)
herd.add(chick1.layer)

canvas.add(herd)
canvas.add(chick2.layer)

for i in range(100):
    herd.move(-5, -2)
    herd.move(-5, 2)
    if i == 30:
        text = Text("OH!", 20)
        text.move(800,160)
        canvas.add(text)
    if i == 40:
        canvas.remove(text)
        text2 = Text("WHERE IS MY MOMMY GOING???", 30)
        text2.move(500,110)
        canvas.add(text2)
    if i == 55:
        canvas.remove(text2)
    if i == 80:
        for i in range(10):
            text3 = Text("Wait for ME~", 25)
            text3.move (500,110)
            canvas.add(text3)
            chick2.wing.adjustReference(-5, -5)
            for i in range(5):
                chick2.layer.move(-10, -20)
                chick2.wing. rotate(-10)
            for i in range(5):
                chick2.layer.move(-10, 20)
                chick2.wing.rotate(10)
        
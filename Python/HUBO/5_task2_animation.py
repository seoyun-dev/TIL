from cs1graphics import *

# canvas
canvas = Canvas(900, 500)
canvas.setBackgroundColor("light sky blue1")
canvas.setTitle("moving animal by PSY")

# 배경
background = Layer()

green_grass = Rectangle(900, 150, Point(450, 425))
green_grass.setFillColor('springgreen2')
green_grass.setBorderColor('springgreen2')
background.add(green_grass)

heart1 = Polygon(Point(200, 70), Point(220, 50), Point( 240, 70), Point(260, 50), Point(280, 70), Point(240, 120))
heart1.setFillColor('hotpink')
heart1.setBorderColor('pink')
background.add(heart1)

heart2 = Polygon(Point(470, 70), Point(490, 50), Point(510, 70), Point(530, 50), Point(550, 70), Point(510, 120))
heart2.setFillColor('hotpink')
heart2.setBorderColor('pink')
background.add(heart2)

canvas.add(background)

# 남자 병아리
boy_chick = Layer()

head = Circle(50, Point(120, 250))
head.setFillColor('Yellow')
head.setBorderColor('Yellow')
boy_chick.add(head)

eye = Ellipse(7, 15, Point(140, 240))
eye.setFillColor('black')
boy_chick.add(eye)

mouse = Polygon(Point(168, 245), Point(183, 255), Point(168, 265))
mouse.setFillColor('brown4')
mouse.setBorderColor('brown4')
mouse.setDepth(60)
boy_chick.add(mouse)

body = Ellipse(140, 110, Point(90, 320))
body.setFillColor('Yellow')
body.setBorderColor('Yellow')
body.setDepth(60) 
boy_chick.add(body)

front_leg =  Rectangle(5, 25, Point(110, 380))
front_leg.setFillColor('brown4')
front_leg.setBorderColor('brown4')
front_leg.setDepth(70)
boy_chick.add(front_leg)

back_leg =  Rectangle(5, 25, Point(70, 380))
back_leg.setFillColor('brown4')
back_leg.setBorderColor('brown4')
back_leg.setDepth(70)
boy_chick.add(back_leg)

front_foot = Ellipse(25, 10, Point(115,395))
front_foot.setFillColor('hotpink')
front_foot.setBorderColor('hotpink')
boy_chick.add(front_foot)

back_foot = Ellipse(25, 10, Point(75,395))
back_foot.setFillColor('blue')
back_foot.setBorderColor('blue')
boy_chick.add(back_foot)

canvas.add(boy_chick)

# 여자 병아리
girl_chick = Layer()
head = Circle(45, Point(780, 250))
head.setFillColor('Yellow')
head.setBorderColor('Yellow')
girl_chick.add(head)

eye = Ellipse(7, 15, Point(760, 240))
eye.setFillColor('black')
girl_chick.add(eye)

eyelash1 = Ellipse(1, 5, Point(763,231))
eyelash1.setFillColor('black')
eyelash1.rotate(45)
girl_chick.add(eyelash1)
eyelash2 = Ellipse(1, 8, Point(764,235))
eyelash2.setFillColor('black')
eyelash2.rotate(55)
girl_chick.add(eyelash2)

mouse = Polygon(Point(735, 245), Point(720, 255), Point(745, 265))
mouse.setFillColor('brown4')
mouse.setBorderColor('brown4')
mouse.setDepth(60)
girl_chick.add(mouse)

body = Ellipse(130, 100, Point(810, 320))
body.setFillColor('Yellow')
body.setBorderColor('Yellow')
body.setDepth(60) 
girl_chick.add(body)

front_leg =  Rectangle(5, 25, Point(790, 380))
front_leg.setFillColor('brown4')
front_leg.setBorderColor('brown4')
front_leg.setDepth(70)
girl_chick.add(front_leg)

back_leg =  Rectangle(5, 25, Point(830, 380))
back_leg.setFillColor('brown4')
back_leg.setBorderColor('brown4')
back_leg.setDepth(70)
girl_chick.add(back_leg)

front_foot = Ellipse(23, 10, Point(785,395))
front_foot.setFillColor('hotpink')
front_foot.setBorderColor('hotpink')
girl_chick.add(front_foot)

back_foot = Ellipse(23, 10, Point(825,395))
back_foot.setFillColor('blue')
back_foot.setBorderColor('blue')
girl_chick.add(back_foot)

canvas.add(girl_chick)

# 첫번째 하트 먹기


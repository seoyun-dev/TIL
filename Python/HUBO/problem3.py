from cs1graphics import *
import math

sin = math.sin
cos = math.cos
pi  = math.pi

# 캔버스 세팅
canvas = Canvas(400, 400)

# 시계
clock        = Layer()
clock_border = Circle(100, Point(200, 200))
clock_border.setFillColor('White')
clock_border.setBorderColor('Black')
clock.add(clock_border)

one    = Text(fontsize=30, message='1', centerPt=Point(200+100*cos((1/3)*pi),200-100*sin((1/3)*pi)))
two    = Text(fontsize=30, message='2', centerPt=Point(200+100*cos((1/6)*pi),200-100*sin((1/6)*pi)))
three  = Text(fontsize=30, message='3', centerPt=Point(200+100*cos((0)*pi),200-100*sin((0)*pi)))
four   = Text(fontsize=30, message='4', centerPt=Point(200+100*cos((-1/6)*pi),200-100*sin((-1/6)*pi)))
five   = Text(fontsize=30, message='5', centerPt=Point(200+100*cos((-1/3)*pi),200-100*sin((-1/3)*pi)))
six    = Text(fontsize=30, message='6', centerPt=Point(200+100*cos((-1/2)*pi),200-100*sin((-1/2)*pi)))
seven  = Text(fontsize=30, message='7', centerPt=Point(200+100*cos((-2/3)*pi),200-100*sin((-2/3)*pi)))
eight  = Text(fontsize=30, message='8', centerPt=Point(200+100*cos((-5/6)*pi),200-100*sin((-5/6)*pi)))
nine   = Text(fontsize=30, message='9', centerPt=Point(200+100*cos((-1)*pi),200-100*sin((-1)*pi)))
ten    = Text(fontsize=30, message='10', centerPt=Point(200+100*cos((5/6)*pi),200-100*sin((5/6)*pi)))
eleven = Text(fontsize=30, message='11', centerPt=Point(200+100*cos((2/3)*pi),200-100*sin((2/3)*pi)))
twelve = Text(fontsize=30, message='12', centerPt=Point(200+100*cos((1/2)*pi),200-100*sin((1/2)*pi)))

clock.add(one)
clock.add(two)
clock.add(three)
clock.add(four)
clock.add(five)
clock.add(six)
clock.add(seven)
clock.add(eight)
clock.add(nine)
clock.add(ten)
clock.add(eleven)
clock.add(twelve)


canvas.add(clock)
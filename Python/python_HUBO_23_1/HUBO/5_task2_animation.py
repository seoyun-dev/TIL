from cs1graphics import *
import time 

################# 캔버스 세팅
canvas = Canvas(900, 500)
canvas.setBackgroundColor("light sky blue1")
canvas.setTitle("moving animal by PSY")


################ 배경
# background layer 위에 그리기
background = Layer()

green_grass = Rectangle(900, 150, Point(450, 425))  # Rectangle의 point는 중심점
green_grass.setFillColor('springgreen2')
green_grass.setBorderColor('springgreen2')
background.add(green_grass)

heart1 = Polygon(Point(200, 70), Point(220, 50), Point( 240, 70), Point(260, 50), Point(280, 70), Point(240, 120))   # polygon의 point는 각 꼭지점
heart1.setFillColor('hotpink')
heart1.setBorderColor('pink')
background.add(heart1)

heart2 = Polygon(Point(470, 70), Point(490, 50), Point(510, 70), Point(530, 50), Point(550, 70), Point(510, 120))
heart2.setFillColor('hotpink')
heart2.setBorderColor('pink')
background.add(heart2)

# canvas에 background layer 추가
canvas.add(background)


################ 병아리랑 하트 
# 남자 병아리 layer 그리기
boy_chick = Layer()

boy_head = Circle(50, Point(120, 250))
boy_head.setFillColor('Yellow')
boy_head.setBorderColor('Yellow')
boy_chick.add(boy_head)

boy_eye = Ellipse(7, 15, Point(140, 240))
boy_eye.setFillColor('black')
boy_chick.add(boy_eye)

boy_mouse = Polygon(Point(168, 245), Point(183, 255), Point(168, 265))
boy_mouse.setFillColor('brown4')
boy_mouse.setBorderColor('brown4')
boy_mouse.setDepth(60)              # Depth 기본값 50
boy_chick.add(boy_mouse)

boy_body = Ellipse(140, 110, Point(90, 320))
boy_body.setFillColor('Yellow')
boy_body.setBorderColor('Yellow')
boy_body.setDepth(60) 
boy_chick.add(boy_body)

boy_front_leg =  Rectangle(5, 25, Point(110, 380))
boy_front_leg.setFillColor('brown4')
boy_front_leg.setBorderColor('brown4')
boy_front_leg.setDepth(70)
boy_chick.add(boy_front_leg)

boy_back_leg =  Rectangle(5, 25, Point(70, 380))
boy_back_leg.setFillColor('brown4')
boy_back_leg.setBorderColor('brown4')
boy_back_leg.setDepth(70)
boy_chick.add(boy_back_leg)

boy_front_foot = Ellipse(25, 10, Point(115,395))
boy_front_foot.setFillColor('hotpink')
boy_front_foot.setBorderColor('hotpink')
boy_chick.add(boy_front_foot)

boy_back_foot = Ellipse(25, 10, Point(75,395))
boy_back_foot.setFillColor('blue')
boy_back_foot.setBorderColor('blue')
boy_chick.add(boy_back_foot)

# canvas에 남자 병아리 layer 추가
canvas.add(boy_chick)

# 여자 병아리 layer 그리기
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

front_leg = Rectangle(5, 25, Point(790, 380))
front_leg.setFillColor('brown4')
front_leg.setBorderColor('brown4')
front_leg.setDepth(70)
girl_chick.add(front_leg)

back_leg = Rectangle(5, 25, Point(830, 380))
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
# canvas에 남자 병아리 layer 추가
canvas.add(girl_chick)

################## 액션
# 첫번째 점프
time.sleep(1)
boy_front_leg.rotate(-30)
boy_front_foot.rotate(-30)
boy_front_foot.move(5,0)
boy_back_leg.rotate(30)
boy_back_foot.rotate(30)
boy_back_foot.move(-5, 0)

for _ in range(100):
    boy_chick.move(1.2, -1.7)

background.remove(heart1)

for _ in range(100):
    boy_chick.move(1.2, 1.7)

boy_front_leg.rotate(30)
boy_front_foot.rotate(30)
boy_front_foot.move(-5,0)
boy_back_leg.rotate(-30)
boy_back_foot.rotate(-30)
boy_back_foot.move(5, 0)

# 두 번째 점프
time.sleep(0.5)
boy_front_leg.rotate(-30)
boy_front_foot.rotate(-30)
boy_front_foot.move(5,0)
boy_back_leg.rotate(30)
boy_back_foot.rotate(30)
boy_back_foot.move(-5, 0)
for _ in range(100):
    boy_chick.move(1.2, -1.7)

background.remove(heart2)

for _ in range(100):
    boy_chick.move(1.2, 1.7)
boy_front_leg.rotate(30)
boy_front_foot.rotate(30)
boy_front_foot.move(-5,0)
boy_back_leg.rotate(-30)
boy_back_foot.rotate(-30)
boy_back_foot.move(5, 0)

# 만나러 가자
for _ in range(60):
    boy_chick.move(1, 0)

# 빅하트 만들고 확대
big_heart = Layer()
heart = Polygon(Point(650, 70), Point(670, 50), Point(690, 70), Point(710, 50), Point(730, 70), Point(690, 120))
heart.setFillColor('hotpink')
heart.setBorderColor('pink')
big_heart.add(heart)
canvas.add(big_heart)

for _ in range(50):
    heart.scale(1.015)
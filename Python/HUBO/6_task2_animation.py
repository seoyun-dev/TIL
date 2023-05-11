from cs1graphics import *

def draw_grass():
    grass = Layer()
    green_grass = Rectangle(900, 150, Point(450, 425))
    green_grass.setFillColor('springgreen2')
    green_grass.setBorderColor('springgreen2')
    grass.add(green_grass)
    return grass

# 동물 생성 후 이동하는 함수. 병렬 이동 말고 다리나 꼬리가 움직이도록.
def draw_animal():
    chick = Layer()
    head = Circle(50, Point(120, 250))
    head.setFillColor('Yellow')
    head.setBorderColor('Yellow')
    chick.add(head)
    
    eye = Ellipse(7, 15, Point(140, 240))
    eye.setFillColor('black')
    chick.add(eye)

    mouse = Polygon(Point(165, 245), Point(180, 255), Point(165, 265))
    mouse.setFillColor('brown4')
    mouse.setBorderColor('brown4')
    mouse.setDepth(60)
    chick.add(mouse)

    body = Ellipse(140, 110, Point(90, 320))
    body.setFillColor('Yellow')
    body.setBorderColor('Yellow')
    body.setDepth(60) 
    chick.add(body)
    
    front_leg =  Rectangle(5, 25, Point(110, 380))
    front_leg.setFillColor('brown4')
    front_leg.setBorderColor('brown4')
    front_leg.setDepth(70)
    chick.add(front_leg)

    back_leg =  Rectangle(5, 25, Point(70, 380))
    back_leg.setFillColor('brown4')
    back_leg.setBorderColor('brown4')
    back_leg.setDepth(70)
    chick.add(back_leg)
    
    front_foot = Ellipse(25, 10, Point(115,395))
    front_foot.setFillColor('hotpink')
    front_foot.setBorderColor('hotpink')
    chick.add(front_foot)

    back_foot = Ellipse(25, 10, Point(75,395))
    back_foot.setFillColor('blue')
    back_foot.setBorderColor('blue')
    chick.add(back_foot)

    return chick

def draw_animal2():
    chick = Layer()
    head = Circle(45, Point(780, 250))
    head.setFillColor('Yellow')
    head.setBorderColor('Yellow')
    chick.add(head)
    
    eye = Ellipse(7, 15, Point(760, 240))
    eye.setFillColor('black')
    chick.add(eye)

    eyelash = Ellipse(1, 5, Point(760,238))
    eyelash.setFillColor('black')
    chick.add(eyelash)

    mouse = Polygon(Point(735, 245), Point(720, 255), Point(745, 265))
    mouse.setFillColor('brown4')
    mouse.setBorderColor('brown4')
    mouse.setDepth(60)
    chick.add(mouse)

    body = Ellipse(130, 100, Point(810, 320))
    body.setFillColor('Yellow')
    body.setBorderColor('Yellow')
    body.setDepth(60) 
    chick.add(body)
    
    front_leg =  Rectangle(5, 25, Point(790, 380))
    front_leg.setFillColor('brown4')
    front_leg.setBorderColor('brown4')
    front_leg.setDepth(70)
    chick.add(front_leg)

    back_leg =  Rectangle(5, 25, Point(830, 380))
    back_leg.setFillColor('brown4')
    back_leg.setBorderColor('brown4')
    back_leg.setDepth(70)
    chick.add(back_leg)
    
    front_foot = Ellipse(25, 10, Point(785,395))
    front_foot.setFillColor('hotpink')
    front_foot.setBorderColor('hotpink')
    chick.add(front_foot)

    back_foot = Ellipse(25, 10, Point(815,395))
    back_foot.setFillColor('blue')
    back_foot.setBorderColor('blue')
    chick.add(back_foot)

    return chick

def show_animation():
    # for 문
    # 뛰어서 하트 물어서 병아리한테 가기
    return


canvas = Canvas(900, 500)
canvas.setBackgroundColor("light sky blue1")
canvas.setTitle("moving animal by PSY")

grass = draw_grass()
canvas.add(grass)

boy_chick = draw_animal()
girl_chick = draw_animal2()
canvas.add(boy_chick)
canvas.add(girl_chick)

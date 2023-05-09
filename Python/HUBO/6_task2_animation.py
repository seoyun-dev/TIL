from cs1graphics import *

def draw_grass():
    grass = Layer()
    green_grass = Rectangle(800, 150, Point(400, 425))
    green_grass.setFillColor('springgreen2')
    green_grass.setBorderColor('springgreen2')
    grass.add(green_grass)
    return grass

# 동물 생성 후 이동하는 함수. 병렬 이동 말고 다리나 꼬리가 움직이도록.
def draw_animal():
    chick = Layer()
    head = Circle(50, Point(30, -80))
    head.setFillColor('Yellow')
    head.setBorderColor('Yellow')
    chick.add(head)
    
    eye = Ellipse(7, 15, Point(50, -90))
    eye.setFillColor('black')
    chick.add(eye)

    mouse = Polygon(Point(60, -80), Point(60, -70), Point(70, -75))
    mouse.setFillColor('black')
    chick.add(mouse)

    body = Ellipse(140, 110, Point(0, -10))
    body.setFillColor('Yellow')
    body.setBorderColor('Yellow')
    body.setDepth(60) 
    chick.add(body)
    # front_foot = 
    return chick

def show_animation():
    # for 문
    return

canvas = Canvas(800, 500)
canvas.setBackgroundColor("light sky blue1")
canvas.setTitle("moving animal by PSY")

grass = draw_grass()
canvas.add(grass)

chick = draw_animal()
canvas.add(chick)
chick.moveTo(100, 300)

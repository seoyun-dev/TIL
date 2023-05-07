from cs1graphics import *
import time


canvas = Canvas(400, 300)                   # 가로 400(왼->오), 세로 300(위->아래)
canvas.setBackgroundColor("light blue")     # color or tuple(r,g,b)
canvas.setTitle("CS101 Drawing exercise")

sq = Square(100)                             # 한 별 길이 100인 사각형
canvas.add(sq)
sq.setFillColor("blue")
sq.setBorderColor("red")
sq.setBorderWidth(5)
sq.moveTo(200, 200)                          # sq.moveTo(절대적 좌표)

time.sleep(1)
for i in range(100):
    sq.move(1, 0)                            # sq.move(상대적 좌표)
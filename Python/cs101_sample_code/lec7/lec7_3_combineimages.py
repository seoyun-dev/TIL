from cs1media import *

def paste(canvas, img, x1, y1):
  w, h = img.size()
  for y in range(h):
    for x in range(w):
      canvas.set(x1 + x, y1 + y, img.get(x, y))

students = load_picture("./cs101_students.jpg")
sejong = load_picture("./sejong.jpg")

students.show()
sejong.show()

paste(students, sejong, 200, 270)
students.show()

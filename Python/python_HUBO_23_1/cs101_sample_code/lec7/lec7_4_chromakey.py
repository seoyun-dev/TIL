from cs1media import *
import math

def dist(c1, c2):
  r1, g1, b1 = c1
  r2, g2, b2 = c2
  return math.sqrt((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2)

def chroma(img, key, threshold):
  w, h = img.size()
  for y in range(h):
    for x in range(w):
      p = img.get(x, y)
      if dist(p, key) < threshold:
        img.set(x, y, Color.yellow)

def chroma_paste(canvas, img, x1, y1, key):
  w, h = img.size()
  for y in range(h):
    for x in range(w):
      p = img.get(x, y)
      if p != key:
        canvas.set(x1 + x, y1 + y, p)


students = load_picture("./cs101_students.jpg")
sejong = load_picture("./sejong.jpg")

students.show()
sejong.show()

chroma(sejong, Color.blue, 200)
sejong.show()

chroma_paste(students, sejong, 200, 270, Color.yellow)
students.show()

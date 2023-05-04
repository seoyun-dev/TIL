from cs1media import *

def luma(p):
  r, g, b = p
  return int(0.213 * r + 0.715 * g + 0.072 * b)

img = load_picture("./cs101_students.jpg")
img.show()
w, h = img.size()
for y in range(h):
  for x in range(w):
    color = img.get(x, y)
    l = luma(color)
    grey = (l, l, l)
    img.set(x, y, grey)
img.show()

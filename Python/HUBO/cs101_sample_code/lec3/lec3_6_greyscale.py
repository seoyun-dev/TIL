from cs1media import *

def luminance(p):
 r, g, b = p
 return int(0.299 * r + 0.587 * g + 0.114 * b)

img = load_picture("./cs101_students.jpg")
img.show()
w, h = img.size()
for y in range(h):
 for x in range(w):
  color = img.get(x, y)
  l = luminance(color)
  grey = (l, l, l)
  img.set(x, y, grey)
img.show()

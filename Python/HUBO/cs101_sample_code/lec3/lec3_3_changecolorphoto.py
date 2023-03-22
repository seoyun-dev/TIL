from cs1media import *

yellow = (255, 255, 0)

img = load_picture("./cs101_students.jpg")
img.show()

img.set(29, 30, yellow)
#img.set(30, 30, yellow)
#img.set(31, 30, yellow)
#img.set(30, 29, yellow)
#img.set(30, 31, yellow)

#w, h = img.size()
#for i in range(w):
#  img.set(i, h/5, yellow)
#  img.set(i, h/5-1, yellow)
#  img.set(i, h/5+1, yellow)

img.show()
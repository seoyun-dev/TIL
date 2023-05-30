# from cs1media import *

# img = load_picture("./cs101_students.jpg")
# img.show()

# w, h = img.size()
# for y in range(h):
#   for x in range(w):
#     r, g, b = img.get(x, y)
#     r, g, b = 255 - r, 255 - g, 255 - b
#     img.set(x, y, (r, g, b))
# img.show()


from cs1media import *

img = load_picture('cs101_students.jpg')
img.show()

w, h = img.size()

purple = (128, 0, 128)
yellow = (255, 255, 0)

for y in range(h):
    for x in range(w):
      r, g, b = img.get(x, y)
      v = (r+g+b) // 3
      if v > 70:
        img.set(x, y, yellow)
      else:
        img.set(x, y, purple)

img.show()
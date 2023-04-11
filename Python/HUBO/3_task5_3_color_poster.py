from cs1media import *

yellow = (255, 255, 0)
green  = (0, 255, 0)
blue   = (0, 0, 255)

img   = load_picture("sonny.jpg")
w, h  = img.size()

for y in range(h):
    for x in range(w):
        r, g, b = img.get(x, y)
        v = (r + g + b) // 3
        if v > 100:
            img.set(x, y, yellow)
        elif v < 30:
            img.set(x, y, blue)
        else:
            img.set(x, y, green)

img.show()
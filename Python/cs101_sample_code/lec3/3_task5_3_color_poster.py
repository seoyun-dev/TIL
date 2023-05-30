from cs1media import *

img = load_picture('sonny.jpg')
img.show()

threshold1 = 100
threshold2 = 30

yellow     = (255, 255, 0)
blue       = (0, 0, 255)
green      = (0, 255, 0)

w, h = img.size()
for y in range(h):
    for x in range(w):
        r, g, b = img.get(x, y)
        v = (r + g + b) // 3
        
        if v > threshold1:
            img.set(x, y, yellow)
        elif v < threshold2:
            img.set(x, y, blue)
        else:
            img.set(x, y, green)

img.show()
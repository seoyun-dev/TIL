from cs1media import *
white = (255, 255, 255)
black = (0, 0, 0)

def luma(p):
  r, g, b = p
  return int(0.213 * r + 0.715 * g + 0.072 * b)

def blackwhite(img, threshold):
  w, h = img.size()
  for y in range(h):
    for x in range(w):
      r, g, b = img.get(x, y)
      if threshold == 0:
        v = luma(img.get(x, y))
        img.set(x,y,(v,v,v))
      else:
        v = (r + g + b) // 3 # average of r,g,b
        if v > threshold:
          img.set(x, y, white)
        else:
          img.set(x, y, black)

img_file_name = raw_input("Enter an image file name> ")
threshold = raw_input("Threshold (0 for grayscale)> ")

pict = load_picture(img_file_name)
pict.show()
blackwhite(pict, int(threshold))
pict.show()


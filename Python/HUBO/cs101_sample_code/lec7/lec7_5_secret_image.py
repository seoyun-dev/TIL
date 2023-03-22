from cs1media import *

def encrypt(img, secret):
 w, h = img.size()
 for y in range(h):
  for x in range(w):
   r, g, b = img.get(x, y)
   if r % 2 == 1:
    img.set(x, y, (r-1, g, b))
 w, h = secret.size()
 for y in range(h):
  for x in range(w):
   sr, sg, sb = secret.get(x, y)
   if sr>200 and sg>200 and sb>200:
    r, g, b = img.get(x, y)
    img.set(x, y, (r+1, g, b))
 return img

def decrypt(img):
 w, h = img.size()
 for y in range(h):
  for x in range(w):
   r, g, b = img.get(x, y)
   if r % 2 == 1:
    img.set(x, y, (255, 255, 255))
   else:
    img.set(x, y, (0, 0, 0))
 return img

pict = load_picture("./Penguins.jpg")
secret_msg = load_picture("./Secret.jpg")
pict = encrypt(pict, secret_msg)
pict.show()
pict = decrypt(pict)
pict.show()


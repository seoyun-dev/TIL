def fun1(x, y):
  a = x
  b = y
  print (a, b)
  return a + b

def fun2(x, y):
  print (a, b)
  x = a
  y = b
  return x + y

a = 10
b = 20
print (a, b)
print (fun1(30, 40))
print (a, b)
print (fun2(30, 40))

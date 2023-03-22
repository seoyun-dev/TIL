import math

def f(x):
 return math.sin(x / 3.0 + math.pi/4.0)

def print_table(func, x0, x1, step):
 x = x0
 while x <= x1:
  print x, func(x)
  x += step
  
print_table(f, -math.pi, 3 * math.pi, math.pi/8)

#print_table(math.sin, -math.pi, 3 * math.pi, math.pi/8)
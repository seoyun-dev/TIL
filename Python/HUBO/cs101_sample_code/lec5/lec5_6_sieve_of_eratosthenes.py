import math

def sieve(n):
  t = range(3, n, 2)
  sqrtn = int(math.sqrt(n))
  i = 0
  while t[i] <=sqrtn:
    #remove all multiples of t[i]
    p = t[i]
    for j in range(len(t)-1, i, -1):
      if t[j] % p == 0:
        t.pop(j)
    i += 1
  return t

while (True):
  num = raw_input("Enter an integer number = ")
  if int(num) < 3:
    break
  print sieve(int(num))

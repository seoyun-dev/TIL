def avg(data, start = 0, end = None):
  if not end:
    print "end = ", end
    end = len(data)
  return sum(data[start:end]) / float(end-start)

d = [ 1, 2, 3, 4, 5 ]
print avg(d)
print avg(d, 2)
print avg(d, 1, 4)
print avg(d, 4, 1)
# print avg(d, 0, 4.5)
print avg(d, 0, '4')

import random


def merge(left, right):
  result = []  # final result list
  i, j = 0, 0

  # keep appending elements into result
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

      # if any element remains in the left list
      # from ith to the last index, we should
      # appended them to result. Same for the right list
  result += left[i:]
  result += right[j:]
  # print(result)
  return result


def merge_sort(a):
  # print(a)
  if len(a) <= 1:
    return a
  m = len(a) // 2
  a1 = a[:m]
  a2 = a[m:]
  l = merge_sort(a1)
  r = merge_sort(a2)
  lst = merge(l, r)
  return lst
  
a = list(range(1, 10000))
random.shuffle(a)
print (a[:100])
a = merge_sort(a)
print (a[:100])

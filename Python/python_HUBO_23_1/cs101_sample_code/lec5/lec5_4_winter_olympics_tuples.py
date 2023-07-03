countries = [ "Australia", "Austria", "Belarus", "Canada", "China", "Croatia", "Czech Republic", "Finland", "France", "Germany", "Great Britain", "Italy", "Japan", "Kazakhstan", "Latvia", "Netherlands", "Norway", "Poland", "Russia", "Slovakia", "Slovenia", "South Korea", "Sweden", "Switzerland", "Ukraine", "United States" ]
gold = [0, 4, 5, 10, 3, 0, 2, 1, 4, 8, 1, 0, 1, 
        0, 0, 8, 11, 4, 13, 1, 2, 3, 2, 6, 1, 9]
silver = [ 2, 8, 0, 10, 4, 1, 4, 3, 4, 6, 1, 2, 4, 0, 
           2, 7, 5, 1, 11, 0, 2, 3, 7, 3, 0, 7]
bronze = [ 1, 5, 1, 5, 2, 0, 2, 1, 7, 5, 2, 6, 3, 1, 
           2, 9, 10, 1, 9, 0, 4, 2, 6, 2, 1, 12]

medals = []
for i in range(len(countries)):
  medals.append( (countries[i], gold[i], silver[i], bronze[i]) )
 
def compare(item1, item2):
  medals1 = sum(item1[1:])
  medals2 = sum(item2[1:])
  return cmp(medals2, medals1)

def compare2(item1, item2):
  if item1[1] < item2[1]:
    return 1
  elif item1[1] == item2[1]:
    if item1[2] < item2[2]:
      return 1
    elif item1[2] == item2[2]:
      if item1[3] < item2[3]:
        return 1
      elif item1[3] == item2[3]:
        return 0 
  return -1

def top_ten():
  medals.sort(compare)
  top_ten = medals[:10]
  for item in top_ten:
    print item[0] + ":", sum(item[1:])

def top_ten2():
  medals.sort(compare2)
  top_ten = medals[:10]
  for item in top_ten:
    print item[0] + ":", item[1], item[2], item[3]
    
top_ten()

countries = [ "Australia", "Austria", "Belarus", "Canada", "China", "Croatia", "Czech Republic", "Finland", "France", "Germany", "Great Britain", "Italy", "Japan", "Kazakhstan", "Latvia", "Netherlands", "Norway", "Poland", "Russia", "Slovakia", "Slovenia", "South Korea", "Sweden", "Switzerland", "Ukraine", "United States" ]
gold = [0, 4, 5, 10, 3, 0, 2, 1, 4, 8, 1, 0, 1, 
        0, 0, 8, 11, 4, 13, 1, 2, 3, 2, 6, 1, 9]
silver = [ 2, 8, 0, 10, 4, 1, 4, 3, 4, 6, 1, 2, 4, 0, 
           2, 7, 5, 1, 11, 0, 2, 3, 7, 3, 0, 7]
bronze = [ 1, 5, 1, 5, 2, 0, 2, 1, 7, 5, 2, 6, 3, 1, 
           2, 9, 10, 1, 9, 0, 4, 2, 6, 2, 1, 12]

def no_medals(countries, a1, b1):
  result = []
  for i in range(len(countries)):
    if a1[i] == 0 and b1[i] == 0:
      result.append(countries[i])
  return result

only_gold = no_medals(countries, silver, bronze)
only_silver = no_medals(countries, gold, bronze)
only_bronze = no_medals(countries, gold, silver)

only_one = only_gold + only_silver + only_bronze

print only_one
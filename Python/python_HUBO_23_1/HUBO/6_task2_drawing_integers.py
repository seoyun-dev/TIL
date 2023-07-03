import random

def drawing_integers(lb, ub, trials):
    num_list = []
    for _ in range(trials):
        num_list.append(random.randint(lb, ub)) # lb <= integers <= ub
    return num_list

def average_integers(num_list):
    return sum(num_list) / len(num_list)

def count_integers(num_list):
    count_list = []
    num_set = set(num_list)
    for i in num_set:
        count_list.append((i, num_list.count(i)))
    return count_list

list1 = drawing_integers(1, 6, 20)
print(list1)
print(average_integers(list1))
print(count_integers(list1))
print()
list2 = drawing_integers(5, 12, 15)
print(list2)
print(average_integers(list2))
print(count_integers(list2))
print()
students = [ ('Kim', 170, 'A'), ('Lee', 182, 'B'), ('Choi', 175, 'B'), ('Park', 168, 'C') ]

def compare1(student1, student2):
   return cmp(student1[1], student2[1])

def compare2(student1, student2):
   if student1[1] > student2[1]:
      if student1[2] < student2[2]:
         return -1
      return 0
   return 1
      
print students
students.sort(compare1)
print students
students.sort(compare2)
print students

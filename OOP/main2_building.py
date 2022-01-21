from calendar import c
from main2 import Student
from main2 import Course

### Adding students
s1 = Student('Baker', 8, 90)
s2 = Student('Servin', 25, 99)
s3 = Student('Camila', 3, 89)

# Making Course
course = Course('Coding 101', 2)

# Adding students to course
course.add_student(s1)
course.add_student(s2)

# adding a third student will return False
print(course.add_student(s3))

# look at the name of first student
print(course.students[0].name)

# look at average grade
print(course.get_average_grade())
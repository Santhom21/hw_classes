from classes import Student, Mentor, Lecturer, Reviewer
from students import oleg, andrey
from mentors import alexander, nikolay, semen, ivan
from functions import make_grades, avg_students_grades, avg_lecturer_grades, compairs

make_grades()

compairs(semen, ivan)

print(avg_students_grades(Student.instances, 'Python'))

print(avg_lecturer_grades(Lecturer.instances, 'Java'))

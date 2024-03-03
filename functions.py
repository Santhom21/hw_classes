from classes import Student, Mentor, Lecturer, Reviewer
from students import oleg, andrey
from mentors import alexander, nikolay, semen, ivan

def make_grades():
    alexander.rate_hw(oleg, 'Python', 8)
    alexander.rate_hw(oleg, 'Python', 9)
    alexander.rate_hw(oleg, 'Java', 8)
    alexander.rate_hw(oleg, 'Java', 9)

    nikolay.rate_hw(andrey, 'Python', 10)
    nikolay.rate_hw(andrey, 'Python', 9)
    nikolay.rate_hw(andrey, 'Java', 9)
    nikolay.rate_hw(andrey, 'Java', 7)

    oleg.rate_lec(semen, 'Python', 10)
    oleg.rate_lec(semen, 'Python', 9)
    oleg.rate_lec(semen, 'Java', 10)
    oleg.rate_lec(semen, 'Java', 9)

    andrey.rate_lec(ivan, 'Python', 10)
    andrey.rate_lec(ivan, 'Python', 9)
    andrey.rate_lec(ivan, 'Java', 8)
    andrey.rate_lec(ivan, 'Java', 8)

def compairs(first, second):
    print(f'{first.name} avg grades = ', first.avgGrades)
    print(f'{second.name} avg grades = ', second.avgGrades)
    print (f'{first.name} < {second.name}', first.avgGrades < second.avgGrades)
    print (f'{first.name} > {second.name}', first.avgGrades > second.avgGrades)
    print (f'{first.name} == {second.name}', first.avgGrades == second.avgGrades)
    print (f'{first.name} != {second.name}', first.avgGrades != second.avgGrades)
    print (f'{first.name} >= {second.name}', first.avgGrades >= second.avgGrades)
    print (f'{first.name} <= {second.name}', first.avgGrades <= second.avgGrades)


def avg_students_grades(students, course):
    all_grades = []
    summ_of_grades = 0
    for student in students:
        if course in student.courses_in_progress:
            if student.avgGrades != 'Нет оценок':
                for course_grade in student.grades[course]:
                    all_grades.append(course_grade)
            else:
                continue
    for grade in all_grades:
        summ_of_grades += grade

    if len(all_grades) > 0:
        return f'На курсе {course} средняя оценка студентов: ' \
        f'{round(summ_of_grades / len(all_grades), 2)}'
    else:
        return f'На курсе {course} нет оценок'


def avg_lecturer_grades(lecturers, course):
    all_grades = []
    summ_of_grades = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            if lecturer.avgGrades != 'Нет оценок':
                for course_grade in lecturer.grades[course]:
                    all_grades.append(course_grade)
            else:
                continue
    for grade in all_grades:
        summ_of_grades += grade

    if len(all_grades) > 0:
        return f'На курсе {course} средняя оценка лекторов: '\
        f'{round(summ_of_grades / len(all_grades), 2)}'
    else:
        return f'На курсе {course} нет оценок'
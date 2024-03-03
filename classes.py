class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
        and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
                student.avgGrades = Student.averageGrades(student)
            else:
                student.grades[course] = [grade]
                student.avgGrades = Student.averageGrades(student)
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"        

class Lecturer(Mentor):
    instances = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.instances.append(self)
        self.avgGrades = Lecturer.averageGrades(self)

    def averageGrades(self):
        all_grades = []
        summ_of_grades = 0
        if len(self.grades) > 0:
            for grades in self.grades.values():
                for i in range(len(grades)):
                    all_grades.append(grades[i])

            for i in range(len(all_grades)):
                summ_of_grades += all_grades[i]
            return summ_of_grades/len(all_grades)
        else:
            return 'Нет оценок'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
            f"Средняя оценка за лекции: {self.averageGrades()}"
    
    def __lt__(self, other):
        return self.averageGrades() < other.averageGrades()
    def __le__(self, other):
        return self.averageGrades() <= other.averageGrades()
    def __eq__(self, other):
        return self.averageGrades() == other.averageGrades()
    def __ne__(self, other):
        return self.averageGrades() != other.averageGrades()
    
    
class Student:
    instances = []
        
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avgGrades = Student.averageGrades(self)
        Student.instances.append(self)

    def rate_lec(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in
        self.courses_in_progress and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                lecturer.avgGrades = Lecturer.averageGrades(lecturer)
            else:
                lecturer.grades[course] = [grade]
                lecturer.avgGrades = Lecturer.averageGrades(lecturer)
        else:
            return 'Ошибка'
        
    def averageGrades(self):
        all_grades = []
        summ_of_grades = 0
        if len(self.grades) > 0:
            for grades in self.grades.values():
                for i in range(len(grades)):
                    all_grades.append(grades[i])

            for i in range(len(all_grades)):
                summ_of_grades += all_grades[i]
            return summ_of_grades/len(all_grades)
        else:
            return 'Нет оценок'

    def __str__(self):
        return f"Имя: {self.name}\n" \
       f"Фамилия: {self.surname}\n" \
       f"Средняя оценка за лекции: {self.averageGrades()}\n" \
       f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
       f"Завершенные курсы: {', '.join(self.finished_courses)}"
    
    def __lt__(self, other):
        return self.averageGrades() < other.averageGrades()
    def __le__(self, other):
        return self.averageGrades() <= other.averageGrades()
    def __eq__(self, other):
        return self.averageGrades() == other.averageGrades()
    def __ne__(self, other):
        return self.averageGrades() != other.averageGrades()
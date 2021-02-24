class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.mean_grade = []

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades_from_students:
                lecturer.grades_from_students[course] += [grade]
            else:
                lecturer.grades_from_students[course] = [grade]
        else:
            return 'Ошибка'


    def mean_grades(self, grade):
        self.grades.mean_grade = (self.grades.values()) / len(self.grades)

    def __str__(self):
        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' + 'Средняя оценка за домашнее задание: ' + self.mean_grades + '\n' + 'Курсы в процессе изучения: ' + self.courses_in_progress + '\n' + 'Завершенные курсы: ' + self.finished_courses


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def _init_(self, name, surname):
        super().__init__(name, surname)
        self.grades_from_students = {}
        self.average_lecturer_grade = []

    def __str__(self):
        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname + '\n' + 'Средняя оценка за лекции: ' + self.average_lecturer_grade

    def average_grade(self):
        self.average_lecturer_grade = (self.grades_from_students.values()) / len(self.grades_from_students)



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return 'Имя: ' + self.name + '\n' + 'Фамилия: ' + self.surname





best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'GIT']
best_student.finished_courses += ['Введение в программирование']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lecturer = Lecturer('Another', 'Girl')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('One', 'Guy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 6)



best_student.rate_lecturer(cool_lecturer, 'Python', 2)

print(cool_lecturer)
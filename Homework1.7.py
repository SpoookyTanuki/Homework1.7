class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.student_mean = 0
    
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades_from_students:
               lecturer.grades_from_students[course] += [grade]
            else:
                lecturer.grades_from_students[course] = [grade]
        else:
            return 'Error'

    def mean_grade(self):
        grades_list = []
        for grade in self.grades.values():
            grades_list += grade
        if grades_list:
            self.student_mean = round(sum(grades_list) / len(grades_list), 1)

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print(other_student.name, " не является студентом!")
        else:
            return self.student_mean < other_student.student_mean
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашнее задание: {str(self.student_mean)}\n' \
               f'Курсы в процессе изучения: {str(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {str(self.finished_courses)}'



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades_from_students = {}
        self.lecturer_mean = 0
        super().__init__(name, surname)

    def mean_grade_from_students(self):
        sum_grade = []
        for grade in self.grades_from_students.values():
            sum_grade += grade
        self.lecturer_mean = str(round(sum(sum_grade) / len(sum_grade), 1))

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print(other_lecturer.name, " не является лектором!")
        else:
            return self.lecturer_mean < other_lecturer.lecturer_mean

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                   f'Средняя оценка за лекции: {str(self.lecturer_mean)}' 


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
            return 'Error'
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Intro to coding']
best_student.finished_courses += ['Git', 'OOP', 'Intro to coding']

so_so_student = Student('Petya', 'Pustota', 'your_gender')
so_so_student.courses_in_progress += ['Python', 'Git']
so_so_student.finished_courses += ['Intro to coding', 'OOP']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python', 'Git', 'Intro to coding', 'OOP']

hot_lecturer = Lecturer('One', 'Girl')
hot_lecturer.courses_attached += ['Python', 'Git', 'Intro to coding', 'OOP']

cool_reviewer = Reviewer('No', 'Way')
cool_reviewer.courses_attached += ['Python', 'Intro to coding', 'Git']

hot_reviewer = Reviewer('Nah', 'Yay')
hot_reviewer.courses_attached += ['Python', 'OOP']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Intro to coding', 6)
cool_reviewer.rate_hw(best_student, 'Intro to coding', 5)
cool_reviewer.rate_hw(best_student, 'Intro to coding', 9)

cool_reviewer.rate_hw(so_so_student, 'Git', 5)
cool_reviewer.rate_hw(so_so_student, 'Git', 4)
cool_reviewer.rate_hw(so_so_student, 'Git', 8)

cool_reviewer.rate_hw(so_so_student, 'Python', 3)
cool_reviewer.rate_hw(so_so_student, 'Python', 9)
cool_reviewer.rate_hw(so_so_student, 'Python', 5)

best_student.rate_lecturer(cool_lecturer, 'Git', 8)
best_student.rate_lecturer(cool_lecturer, 'OOP', 9)

best_student.rate_lecturer(hot_lecturer, 'Git', 10)
best_student.rate_lecturer(hot_lecturer, 'OOP', 9)

so_so_student.rate_lecturer(cool_lecturer, 'Intro to coding', 5)
so_so_student.rate_lecturer(cool_lecturer, 'OOP', 5)

so_so_student.rate_lecturer(cool_lecturer, 'Intro to coding', 5)
so_so_student.rate_lecturer(cool_lecturer, 'OOP', 5)

best_student.mean_grade()
so_so_student.mean_grade()
print(best_student.student_mean)
print(so_so_student.student_mean)
print(best_student.student_mean > so_so_student.student_mean)
print()

cool_lecturer.mean_grade_from_students()
hot_lecturer.mean_grade_from_students()

print(cool_lecturer.lecturer_mean)
print(hot_lecturer.lecturer_mean)
print(cool_lecturer.lecturer_mean < hot_lecturer.lecturer_mean)
print()

print(best_student)
print()
print(so_so_student)
print()

print(cool_lecturer)
print()
print(hot_lecturer)
print()

print(cool_reviewer)
print()
print(hot_reviewer)
print()

def all_mean_stud(students_list, course_name):
    all_grades = list()
    for student in students_list:
        for val in student.grades[course_name]:
            all_grades.append(val)
    course_result = round((sum(all_grades) / len(all_grades)), 1)
    return course_result
    
print(all_mean_stud([best_student, so_so_student], 'Python'))


def all_mean_lect(lect_list, course_name):
    all_grades = list()
    for lecturer in lect_list:
        for val in lecturer.grades_from_students[course_name]:
            all_grades.append(val)
    course_result = round((sum(all_grades) / len(all_grades)), 1)
    return course_result
    
print(all_mean_lect([cool_lecturer, hot_lecturer], 'OOP'))


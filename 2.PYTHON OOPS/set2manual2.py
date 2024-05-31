'''A program that simulates a school management system, with classes for the 
students, the teachers, and the courses.'''

class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        course.students.append(self)

    def get_courses(self):
        return [course.name for course in self.courses]


class Teacher:
    def __init__(self, name, age, teacher_id):
        self.name = name
        self.age = age
        self.teacher_id = teacher_id
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)
        course.teacher = self

    def get_courses(self):
        return [course.name for course in self.courses]


class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id
        self.students = []
        self.teacher = None

    def get_students(self):
        return [student.name for student in self.students]

    def get_teacher(self):
        return self.teacher.name if self.teacher else None

#Usage:
student1 = Student("Akarsh", 20, "S101")
student2 = Student("Nitish", 22, "S102")
teacher1 = Teacher("Sandeep Sir", 30, "T101")
course1 = Course("Mathematics", "C101")
student1.enroll(course1)
teacher1.assign_course(course1)
print(course1.get_students())  
print(course1.get_teacher())  
print(student1.get_courses())  

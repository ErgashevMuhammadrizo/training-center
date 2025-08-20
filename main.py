
# Entity (Model) classlar
class User:
    def __init__(self, id, fullname, username, password, role):
        self.id = id
        self.fullname = fullname
        self.username = username
        self.password = password
        self.role = role

class Admin(User):
    def __init__(self, id, fullname, username, password):
        super().__init__(id, fullname, username, password, role="admin")

class Teacher(User):
    def __init__(self, id, fullname, username, password, skills=None):
        super().__init__(id, fullname, username, password, role="teacher")
        self.skills = skills or []

class Student(User):
    def __init__(self, id, fullname, username, password, level=None):
        super().__init__(id, fullname, username, password, role="student")
        self.level = level

class Course:
    def __init__(self, id, title, price, duration_weeks):
        self.id = id
        self.title = title
        self.price = price
        self.duration_weeks = duration_weeks

class Group:
    def __init__(self, id, name, course_id, teacher_id, student_ids=None):
        self.id = id
        self.name = name
        self.course_id = course_id
        self.teacher_id = teacher_id
        self.student_ids = student_ids or []

class Homework:
    def __init__(self, id, group_id, title, description, deadline):
        self.id = id
        self.group_id = group_id
        self.title = title
        self.description = description
        self.deadline = deadline

class Grade:
    def __init__(self, id, homework_id, student_id, value):
        self.id = id
        self.homework_id = homework_id
        self.student_id = student_id
        self.value = value

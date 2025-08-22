
# Entity (Model) classlar

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

# In-memory demo DB
users = [
    Admin(1, "Admin One", "admin", "123"),
    Teacher(2, "Ali Teacher", "ali", "123", skills=["Math"]),
    Student(3, "Laylo Student", "laylo", "123", level="A")
]
courses = [Course(1, "Python", 1000000, 12)]
groups = []
homeworks = []
grades = []

def find_user(username, password):
    for u in users:
        if u.username == username and u.password == password:
            return u
    return None

def admin_menu(admin):
    while True:
        print("\n--- Admin menyu ---")
        print("1) Teacher qo'shish")
        print("2) Student qo'shish")
        print("3) Guruh ochish")
        print("4) Teacher biriktirish")
        print("5) Guruhga student qo'shish")
        print("6) Barcha guruhlarni ko'rish")
        print("7) Barcha teacherlarni ko'rish")
        print("8) Barcha studentlarni ko'rish")
        print("9) Studentning guruhlarini ko'rish")
        print("10) Teacherning guruhlarini ko'rish")
        print("0) Chiqish")
        c = input("Tanlang: ")
        if c == "1":
            fullname = input("Teacher FIO: ")
            username = input("Username: ")
            password = input("Password: ")
            skills = input("Skills (vergul bilan): ").split(",")
            uid = max([u.id for u in users]+[0])+1
            users.append(Teacher(uid, fullname, username, password, skills))
            print("Teacher qo'shildi!")
        elif c == "2":
            fullname = input("Student FIO: ")
            username = input("Username: ")
            password = input("Password: ")
            level = input("Level: ")
            uid = max([u.id for u in users]+[0])+1
            users.append(Student(uid, fullname, username, password, level))
            print("Student qo'shildi!")
        elif c == "3":
            name = input("Guruh nomi: ")
            course_id = int(input("Kurs ID: "))
            gid = max([g.id for g in groups]+[0])+1
            groups.append(Group(gid, name, course_id, None))
            print("Guruh ochildi!")
        elif c == "4":
            gid = int(input("Guruh ID: "))
            tid = int(input("Teacher ID: "))
            for g in groups:
                if g.id == gid:
                    g.teacher_id = tid
                    print("Biriktirildi!")
                    break
        elif c == "5":
            gid = int(input("Guruh ID: "))
            sid = int(input("Student ID: "))
            for g in groups:
                if g.id == gid:
                    if sid not in g.student_ids:
                        g.student_ids.append(sid)
                        print("Qo'shildi!")
                    else:
                        print("Bu student allaqachon guruhda!")
                    break
        elif c == "6":
            print("\n--- Barcha guruhlar ---")
            for g in groups:
                tname = next((u.fullname for u in users if isinstance(u, Teacher) and u.id == g.teacher_id), "-")
                print(f"ID:{g.id} {g.name} | KursID:{g.course_id} | Teacher:{tname} | Students:{g.student_ids}")
        elif c == "7":
            print("\n--- Barcha teacherlar ---")
            for u in users:
                if isinstance(u, Teacher):
                    print(f"ID:{u.id} {u.fullname} | Skills: {', '.join(u.skills)}")
        elif c == "8":
            print("\n--- Barcha studentlar ---")
            for u in users:
                if isinstance(u, Student):
                    print(f"ID:{u.id} {u.fullname} | Level: {u.level}")
        elif c == "9":
            sid = int(input("Student ID: "))
            print(f"Student ID {sid} guruhlari:")
            for g in groups:
                if sid in g.student_ids:
                    print(f"ID:{g.id} {g.name}")
        elif c == "10":
            tid = int(input("Teacher ID: "))
            print(f"Teacher ID {tid} guruhlari:")
            for g in groups:
                if g.teacher_id == tid:
                    print(f"ID:{g.id} {g.name}")
        elif c == "0":
            break
        else:
            print("Noto'g'ri tanlov!")

def teacher_menu(teacher):
    while True:
        print("\n--- Teacher menyu ---")
        print("1) Guruhlarim")
        print("2) Guruhdagi studentlar")
        print("3) Uyga vazifa joylash")
        print("4) Baho qo'yish")
        print("0) Chiqish")
        c = input("Tanlang: ")
        if c == "1":
            print("Sizning guruhlaringiz:")
            for g in groups:
                if g.teacher_id == teacher.id:
                    print(f"ID:{g.id} {g.name}")
        elif c == "2":
            gid = int(input("Guruh ID: "))
            group = next((g for g in groups if g.id == gid and g.teacher_id == teacher.id), None)
            if group:
                print(f"Guruh: {group.name}")
                for sid in group.student_ids:
                    s = next((u for u in users if isinstance(u, Student) and u.id == sid), None)
                    if s:
                        print(f"ID:{s.id} {s.fullname} | Level: {s.level}")
            else:
                print("Bunday guruh topilmadi yoki sizga tegishli emas!")
        elif c == "3":
            gid = int(input("Guruh ID: "))
            group = next((g for g in groups if g.id == gid and g.teacher_id == teacher.id), None)
            if not group:
                print("Bunday guruh topilmadi yoki sizga tegishli emas!")
                continue
            title = input("Vazifa nomi: ")
            desc = input("Tavsif: ")
            deadline = input("Deadline: ")
            hid = max([h.id for h in homeworks]+[0])+1
            homeworks.append(Homework(hid, gid, title, desc, deadline))
            print("Vazifa joylandi!")
        elif c == "4":
            gid = int(input("Guruh ID: "))
            group = next((g for g in groups if g.id == gid and g.teacher_id == teacher.id), None)
            if not group:
                print("Bunday guruh topilmadi yoki sizga tegishli emas!")
                continue
            hid = int(input("Homework ID: "))
            homework = next((h for h in homeworks if h.id == hid and h.group_id == gid), None)
            if not homework:
                print("Bunday homework topilmadi!")
                continue
            sid = int(input("Student ID: "))
            if sid not in group.student_ids:
                print("Bu student bu guruhda emas!")
                continue
            value = input("Baho: ")
            gid_grade = max([g.id for g in grades]+[0])+1
            grades.append(Grade(gid_grade, hid, sid, value))
            print("Baho qo'yildi!")
        elif c == "0":
            break
        else:
            print("Noto'g'ri tanlov!")

def student_menu(student):
    while True:
        print("\n--- Student menyu ---")
        print("1) Guruhlarim")
        print("2) Guruhdagi studentlar (faqat o'zi a'zo bo'lgan)")
        print("3) Uyga vazifalarim")
        print("4) Baholarim")
        print("0) Chiqish")
        c = input("Tanlang: ")
        if c == "1":
            print("Siz a'zo bo'lgan guruhlar:")
            for g in groups:
                if student.id in g.student_ids:
                    tname = next((u.fullname for u in users if isinstance(u, Teacher) and u.id == g.teacher_id), "-")
                    print(f"ID:{g.id} {g.name} | Teacher: {tname}")
        elif c == "2":
            gid = int(input("Guruh ID: "))
            group = next((g for g in groups if g.id == gid and student.id in g.student_ids), None)
            if group:
                print(f"Guruh: {group.name}")
                for sid in group.student_ids:
                    s = next((u for u in users if isinstance(u, Student) and u.id == sid), None)
                    if s:
                        print(f"ID:{s.id} {s.fullname} | Level: {s.level}")
            else:
                print("Bunday guruh topilmadi yoki siz a'zo emassiz!")
        elif c == "3":
            print("Siz uchun uyga vazifalar:")
            for g in groups:
                if student.id in g.student_ids:
                    for h in homeworks:
                        if h.group_id == g.id:
                            print(f"ID:{h.id} {h.title} ({h.deadline})")
        elif c == "4":
            print("Sizning baholaringiz:")
            for gr in grades:
                if gr.student_id == student.id:
                    print(f"HomeworkID:{gr.homework_id} Baho:{gr.value}")
        elif c == "0":
            break
        else:
            print("Noto'g'ri tanlov!")

def main():
    print("\nO'quv markazi CLI tizimi!")
    while True:
        username = input("Login: ")
        password = input("Parol: ")
        user = find_user(username, password)
        if user:
            print(f"Xush kelibsiz, {user.fullname}! Rol: {user.role}")
            if user.role == "admin":
                admin_menu(user)
            elif user.role == "teacher":
                teacher_menu(user)
            elif user.role == "student":
                student_menu(user)
        else:
            print("Login yoki parol xato!")

if __name__ == "__main__":
    main()

# 🎓 O‘quv Markazi Tizimi — Terminal (CLI) Loyihasi

> **Maqsad:** Admin, Teacher va Student rollari bilan ishlaydigan terminal tizim.  
> **Usul:** Har bir funksiya uchun **alohida class** (SRP — Single Responsibility) qo‘llaniladi.  
> **Fayl:** README.md — VS Code’da chiroyli ko‘rinishda o‘qilishi uchun yozildi.

---

## 🧭 Tez Ko‘rinish (Executive Summary)
- **Rollar:** `Admin`, `Teacher`, `Student`
- **Asosiy imkoniyatlar:**
  - Admin → o‘qituvchi/talaba qo‘shish, guruh ochish, bog‘lash
  - Teacher → guruhlarini ko‘rish, uyga vazifa joylash, baholash
  - Student → uyga vazifalar va baholarni ko‘rish
- **Arxitektura:** Entity classlar + *Har-funktsiya-uchun-class* (Service/Action classlar)
- **Saqlash:** JSON fayllar (oddiy demo uchun)

---

## 🧩 Rollar va Funksiyalar

### 👑 Admin
- Teacher qo‘shish / o‘chirish
- Student qo‘shish / o‘chirish
- Guruh ochish / o‘chirish
- Guruhga Teacher biriktirish
- Guruhga Student qo‘shish
- Kurs qo‘shish / narxini o‘zgartirish

### 👨‍🏫 Teacher
- O‘z guruhlarini ko‘rish
- Guruh uchun uyga vazifa (homework) joylash
- Talabalarga baho qo‘yish
- Guruhdagi talabalar ro‘yxatini ko‘rish

### 👩‍🎓 Student
- O‘zi a’zo bo‘lgan guruh(lar)ni ko‘rish
- Uyga vazifalarni ko‘rish
- Baholarini ko‘rish

---

## 🏗️ Class Dizayn (SRP — **har bir funksiya uchun alohida class**)

### 1) **Entity (Model) classlar**
- `User` (id, fullname, username, password, role)
- `Admin` (User dan meros)
- `Teacher` (User dan meros, skills)
- `Student` (User dan meros, level)
- `Course` (id, title, price, duration_weeks)
- `Group` (id, name, course_id, teacher_id, student_ids[])
- `Homework` (id, group_id, title, description, deadline)
- `Grade` (id, homework_id, student_id, value)

### 2) **Action/Service classlar (har funksiya uchun bitta class)**
> Quyida minimal, lekin kengaytiriladigan ro‘yxat berildi.

**Admin amallari:**
- `AdminAddTeacher`
- `AdminRemoveTeacher`
- `AdminAddStudent`
- `AdminRemoveStudent`
- `AdminCreateGroup`
- `AdminDeleteGroup`
- `AdminAssignTeacherToGroup`
- `AdminAddStudentToGroup`
- `AdminAddCourse`
- `AdminUpdateCoursePrice`

**Teacher amallari:**
- `TeacherListGroups`
- `TeacherPostHomework`
- `TeacherGradeHomework`
- `TeacherListStudentsInGroup`

**Student amallari:**
- `StudentViewGroups`
- `StudentViewHomeworks`
- `StudentViewGrades`

**Yordamchi:**
- `AuthLogin` (rolga qarab sessiya)
- `MenuRouter` (rolga mos menyu)
- `Storage` (JSON o‘qish/yozish)
- `IdGenerator`, `Validator`, `Clock`

> **Afzallik:** Har bir class faqat **bitta ish** qiladi — testlash va kengaytirish oson.

---

## 🔗 Bog‘lanish Diagrammasi (ASCII UML)

```
User <|-- Admin
User <|-- Teacher
User <|-- Student

Course 1---* Group
Teacher 1---* Group
Group 1---* Homework
Student *---* Group   (student_ids[] ichida)
Homework 1---* Grade
Student 1---* Grade
```

---

## 🧪 CLI Flow (oddiy)

```
Start
 └── Login (AuthLogin)
      ├── Admin → MenuRouter(Admin)
      │     ├── Teacher qo‘shish (AdminAddTeacher)
      │     ├── Student qo‘shish (AdminAddStudent)
      │     ├── Guruh ochish (AdminCreateGroup)
      │     ├── Teacher biriktirish (AdminAssignTeacherToGroup)
      │     └── Guruhga student qo‘shish (AdminAddStudentToGroup)
      │
      ├── Teacher → MenuRouter(Teacher)
      │     ├── Guruhlarim (TeacherListGroups)
      │     ├── Uyga vazifa joylash (TeacherPostHomework)
      │     └── Baho qo‘yish (TeacherGradeHomework)
      │
      └── Student → MenuRouter(Student)
            ├── Guruhlarim (StudentViewGroups)
            ├── Uyga vazifalar (StudentViewHomeworks)
            └── Baholarim (StudentViewGrades)
```

---

## 🗂️ JSON Saqlash Strukturasi (misol)

```
data/
 ├── users.json        # Admin/Teacher/Student
 ├── courses.json
 ├── groups.json
 ├── homeworks.json
 └── grades.json
```

**users.json (sample):**
```json
[
  {"id": 1, "fullname": "Admin One", "username": "admin", "password": "123", "role": "admin"},
  {"id": 2, "fullname": "Ali Teacher", "username": "ali", "password": "123", "role": "teacher"},
  {"id": 3, "fullname": "Laylo Student", "username": "laylo", "password": "123", "role": "student"}
]
```

---

## 🧱 Minimal Folder Strukturasi

```
project-root/
 ├── app/
 │   ├── entities/          # Model classlar
 │   ├── actions/           # Har-funktsiya-uchun classlar
 │   ├── core/              # Storage, MenuRouter, AuthLogin
 │   └── main.py            # CLI kirish nuqtasi
 ├── data/                  # JSON fayllar
 └── README.md              # Shu fayl
```

---

## 📝 Command-Line UI (namuna prompt matnlari)

- **Admin menyu:**
  - 1) Teacher qo‘shish
  - 2) Student qo‘shish
  - 3) Guruh ochish
  - 4) Teacher biriktirish
  - 5) Guruhga student qo‘shish
  - 0) Chiqish

- **Teacher menyu:**
  - 1) Guruhlarim
  - 2) Uyga vazifa joylash
  - 3) Baho qo‘yish
  - 0) Chiqish

- **Student menyu:**
  - 1) Guruhlarim
  - 2) Uyga vazifalarim
  - 3) Baholarim
  - 0) Chiqish

---

## ✅ Qoidalar (Design Principles)
- **SRP:** Har funksiya → bitta class
- **Open/Closed:** Yangi funksiya qo‘shish — yangi class qo‘shish
- **Separation of Concerns:** Entity ↔ Action ↔ Storage aniq ajratilgan
- **Testability:** Har bir Action class alohida test qilinadi

---

## 🚀 Keyingi Qadamlar
- `main.py` da menyularni `MenuRouter` orqali bog‘lash
- `Storage` bilan JSON CRUD yozish
- Har bir Action class uchun unit-test

> Agar xohlasangiz, shu strukturaga mos **ishlaydigan minimal CLI kod**ni ham tayyorlab bera olaman.
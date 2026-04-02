class User:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return f"User: {self.name}"


class Student(User):
    def __init__(self, name):
        super().__init__(name)
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} {course} kursiga yozildi.")

    def show_courses(self):
        print(f"{self.name} kurslari:")
        for c in self.courses:
            print("-", c)


class Teacher(User):
    def __init__(self, name):
        super().__init__(name)
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print(f"{course} kursi qo'shildi.")

    def show_courses(self):
        print(f"{self.name} o'qitadigan kurslar:")
        for c in self.courses:
            print("-", c)


def run_course_system():
    t = Teacher("Ustoz Ali")
    s = Student("Vali")

    t.add_course("Python")
    t.add_course("AI")

    s.enroll("Python")

    t.show_courses()
    s.show_courses()


run_course_system()

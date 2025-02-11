class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.enrolled_courses = []

    def enroll(self, course):
        self.enrolled_courses.append(course)

    def display_details(self):
        details = super().display_details()
        courses = ", ".join(self.enrolled_courses) if self.enrolled_courses else "No courses enrolled"
        return f"{details}, Student ID: {self.student_id}, Courses: {courses}"


class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.assigned_courses = []

    def assign_course(self, course):
        self.assigned_courses.append(course)

    def display_details(self):
        details = super().display_details()
        courses = ", ".join(self.assigned_courses) if self.assigned_courses else "No courses assigned"
        return f"{details}, Teacher ID: {self.teacher_id}, Courses: {courses}"


class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.students = []
        self.teacher = None

    def add_student(self, student):
        self.students.append(student)

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def display_details(self):
        students = ", ".join([student.name for student in self.students]) if self.students else "No students enrolled"
        teacher = self.teacher.name if self.teacher else "No teacher assigned"
        return f"Course Name: {self.course_name}, Code: {self.course_code}, Teacher: {teacher}, Students: {students}"


class College(Student, Teacher, Course):
    def __init__(self, college_name):
        self.college_name = college_name
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def display_college_details(self):
        print(f"College: {self.college_name}")
        print("\nStudents:")
        for student in self.students:
            print(student.display_details())
        print("\nTeachers:")
        for teacher in self.teachers:
            print(teacher.display_details())
        print("\nCourses:")
        for course in self.courses:
            print(course.display_details())


if __name__ == "__main__":
    
    college = College("Tech Institute")

    math = Course("Maths", "101")
    science = Course("Science", "102")

    student1 = Student("Aakash", 19, "001")
    student2 = Student("Bhagyesh", 19, "002")

    teacher1 = Teacher("Ms. Anita", 33, "P001")

    college.add_student(student1)
    college.add_student(student2)
    college.add_teacher(teacher1)
    college.add_course(math)
    college.add_course(science)

    math.assign_teacher(teacher1)
    teacher1.assign_course("Maths")

    student1.enroll("Maths")
    math.add_student(student1)

    student2.enroll("Science")
    science.add_student(student2)

    college.display_college_details()

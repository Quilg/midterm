import csv
from course import Course
from student import Student
from enrollment import Enrollment

class School:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.enrollments = []

    def files(self):
        with open('files/students.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                student = Student(row[0], row[1], row[2])
                self.students[row[0]] = student

        with open('files/courses.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                course = Course(row[0], row[1], row[2])
                self.courses[row[0]] = course

        with open('files/enrollments.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                enrollment = Enrollment(row[0], row[1], row[2], row[3])
                self.enrollments.append(enrollment)

    def menu(self):
        print("1. Add Student")
        print("2. Enroll Student to Course")
        print("3. Grade Student")
        print("4. Display Student")
        print("5. Display Course")
        print("0. EXIT")

    def add(self):
        id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        email = input("Enter Student Email: ")
        student = Student(id, name, email)
        self.students[id] = student
        print("Student Added!")

    def enroll(self):
        student_id = input("Enter Student ID: ")
        if student_id not in self.students:
            print("Student not found")
            return
        course_id = input("Enter Course ID: ")
        if course_id not in self.courses:
            print("Course not found")
            return
        semester = input("Enter Semester: ")
        enrollment = Enrollment(student_id, course_id, semester, "")
        self.enrollments.append(enrollment)
        self.students[student_id].courses[course_id] = semester
        self.courses[course_id].students[student_id] = semester
        print("Student Enrolled!")

    def grade(self):
        student_id = input("Enter Student ID: ")
        course_id = input("Enter Course ID: ")
        grade = input("Enter Grade: ")
        for enrollment in self.enrollments:
            if enrollment.student_id == student_id and enrollment.course_id == course_id:
                enrollment.grade = grade
                self.students[student_id].courses[course_id] = grade
                self.courses[course_id].students[student_id] = grade
                print("Grade Assigned!")
                return
        print("This Student is not enrolled in this Course")

    def display_student(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            student = self.students[student_id]
            print("Student ID:", student.id)
            print("Student Name:", student.name)
            print("Student Email:", student.email)
            print("Courses Enrolled:")
            for enrollment in self.enrollments:
                if enrollment.student_id == student_id:
                    course_id = enrollment.course_id
                    semester = enrollment.semester
                    grade = enrollment.grade
                    if grade is None:
                        grade = "N/A"
                    print(course_id, "-", self.courses[course_id].name, "-", semester, "-", self.courses[course_id].credit, "credits", "-", grade)
        else:
            print("Student not found")


    def display_course(self):
        course_id = input("Enter Course ID: ")
        if course_id in self.courses:
            course = self.courses[course_id]
            print("Course ID:", course.id)
            print("Course Name:", course.name)
            print("Course Credit:", course.credit)
            print("Students Enrolled:")
            for enrollment in self.enrollments:
                if enrollment.course_id == course_id:
                    student_id = enrollment.student_id
                    semester = enrollment.semester
                    grade = enrollment.grade
                    if grade is None:
                        grade = "N/A"
                    print(student_id, "-", self.students[student_id].name, "-", semester, "-", grade)
            else:
                print("No-one is enrolled into this course") #Not working for some reason. Even if there are enrollments, it still prints the prompt
        else:
            print("Course not found")

    def run(self):
        self.files()
        while True:
            self.menu()
            choice = int(input("Select: "))
            if choice == 1:
                self.add()
            elif choice == 2:
                self.enroll()
            elif choice == 3:
                self.grade()
            elif choice == 4:
                self.display_student()
            elif choice == 5:
                self.display_course()
            elif choice == 0:
                print("Goodbye!")
                break

school = School()
school.run()
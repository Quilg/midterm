import csv
from Student import Student
from Courses import Course
from Enrollments import Enrollment

def data():
    students = {}
    courses = {}

    with open('files/students.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) 
        for row in reader:
            id, name, email = row
            students[id] = Student(id, name, email)

    with open('files/courses.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) 
        for row in reader:
            id, name, credit = row
            courses[id] = Course(id, name, credit)

    with open('files/enrollments.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            student_id, course_id, semester, grade = row
            enrollment = Enrollment(student_id, course_id, semester, grade)
            students[student_id].enrollments.append(enrollment)
            courses[course_id].enrollments.append(enrollment)
            

    return students, courses

def add(students):
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    email = input("Enter student email: ")
    students[id] = Student(id, name, email)

def enroll(students, courses):
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    semester = input("Enter semester: ")
    enrollment = Enrollment(student_id, course_id, semester)
    students[student_id].enrollments.append(enrollment)
    courses[course_id].enrollments.append(enrollment)
    

def grade(students):
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    semester = input("Enter semester: ") #maybe the person took the course multiple times, so it checks the correct semester
    grade = input("Enter grade: ")
    for enrollment in students[student_id].enrollments:
        if enrollment.course_id == course_id and enrollment.semester == semester:
            enrollment.grade = grade
            break

def display_student(students):
    id = input("Enter student ID: ")
    student = students.get(id)
    if student:
        print("--------------")
        print(f"ID: {student.id}")
        print(f"Name: {student.name}")
        print(f"Email: {student.email}")
        print("--------------")
        print("Courses: ")
        for enrollment in student.enrollments:
            course = courses.get(enrollment.course_id)
            if course:
                if enrollment.grade is None:
                    enrollment.grade = "N/A" #if the grade is empty, it will add "N/A" as it is in the csv file
                print(f"{course.id} - {course.name} - {enrollment.semester} - {course.credit} credits - {enrollment.grade}")

    else:
        print("Student not found")

def display_course(courses):    
    id = input("Enter course ID: ")
    course = courses.get(id)
    if course:
        print("--------------")
        print(f"ID: {course.id}")
        print(f"Name: {course.name}")
        print(f"Credit: {course.credit}")
        print("--------------")
        enrollments = course.enrollments
        if enrollments:
            print("Students: ")
            for enrollment in enrollments:
                student = students.get(enrollment.student_id)
                if student:
                    print(f"{student.id} - {student.name} - {enrollment.semester} - {enrollment.grade}")
                else:
                    print("Student not found")
        else:
            print("No-one is enrolled into this course.")
    else:
        print("Course not found")


students, courses = data() #loads data

while True:
    print("1. Add Student")
    print("2. Enroll Student to Course")
    print("3. Grade Student")
    print("4. Display Student")
    print("5. Display Course")
    print("0. EXIT")

    choice = input("Enter your choice: ")
    if choice == '1':
        add(students)
    elif choice == '2':
        enroll(students, courses)
    elif choice == '3':
        grade(students)
    elif choice == '4':
        display_student(students)
    elif choice == '5':
        display_course(courses)
    elif choice == '0':
        print("Goodbye!")
        break
    else:
        print("Wrong choice")


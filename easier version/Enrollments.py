
class Enrollment:
    def __init__(self, student_id, course_id, semester, grade=None):
        self.student_id = student_id
        self.course_id = course_id
        self.semester = semester
        self.grade = grade
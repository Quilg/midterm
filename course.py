
class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit
        self.students = {}
        self.semester = None
        self.grade = None
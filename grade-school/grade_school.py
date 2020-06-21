class School:

    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        self.students[name] = grade
        self.students = dict(sorted(
            self.students.items(), key=lambda student_grade:
                str(student_grade[1]) + student_grade[0]
        ))

    def roster(self):
        return [student for student in self.students]

    def grade(self, grade_number):
        return [
            student for student in self.students
            if self.students[student] == grade_number
        ]

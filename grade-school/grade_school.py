class School:

    def __init__(self):
        self.students = {}
        self.students_sorted = []

    def add_student(self, name, grade):
        self.students[name] = grade
        self.students_sorted = sorted(
            self.students.items(), key=lambda student_grade:
                str(student_grade[1]) + student_grade[0]
        )

    def roster(self):
        return [student[0] for student in self.students_sorted]

    def grade(self, grade_number):
        return [
            student[0]
            for student
            in self.students_sorted
            if student[1] == grade_number
        ]

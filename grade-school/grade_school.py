class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        self.students[name] = grade

    def roster(self):
        grades_to_students = {}
        roster = []
        for name, grade in self.students.items():
            if grade in grades_to_students:
                grades_to_students[grade].append(name)
            else:
                grades_to_students[grade] = [name]
        for key in sorted(grades_to_students.keys()):
            roster += sorted(grades_to_students[key])
        return roster

    def grade(self, grade_number):
        return sorted([
            student for student in self.students.keys()
            if self.students[student] == grade_number
        ])

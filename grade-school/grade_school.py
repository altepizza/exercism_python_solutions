class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        self.students.append({name: grade})

    def roster(self):
        grades_to_students = {}
        roster = []
        for student in self.students:
            name, grade = student.items()[0]
            if grade in grades_to_students:
                grades_to_students[grade].append(name)
            else:
                grades_to_students[grade] = [name]
        for key in sorted(grades_to_students.keys()):
            roster = roster + sorted(grades_to_students[key])
        return roster

    def grade(self, grade_number):
        return sorted([
            student.keys()[0] for student in self.students 
            if student[student.keys()[0]] == grade_number
        ])
 

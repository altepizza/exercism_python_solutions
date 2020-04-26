class Garden:
    DEFAULT_CLASS = [
        'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 
        'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]
    CHAR_TO_PLANT = {
        'V': 'Violets', 'R': 'Radishes', 'G': 'Grass', 'C': 'Clover'
    }

    def __init__(self, diagram, students=None):
        students = sorted(students or self.DEFAULT_CLASS)
        diagram = diagram.splitlines()
        self.student_to_plant = {}
        for idx, student in enumerate(students):
            start = idx * 2
            if start+1 >= len(diagram[0]):
                break
            chars = [
                diagram[0][start], diagram[0][start+1],
                diagram[1][start], diagram[1][start+1]
            ]
            self.student_to_plant[student] = [
                self.CHAR_TO_PLANT[char] for char in chars
            ]

    def plants(self, student):
        return self.student_to_plant[student]
        
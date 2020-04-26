class Matrix(object):

    def __init__(self, matrix_string):
        self.aMatrix = [[int(value) for value in row.split(' ')] for row in matrix_string.split('\n')]

    def row(self, index):
        return [cell for cell in self.aMatrix[index-1]]

    def column(self, index):
        return [row[index-1] for row in self.aMatrix]

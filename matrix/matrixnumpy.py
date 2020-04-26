class Matrix(object):

    def __init__(self, matrix_string):
        print ('-'*10)
        self.aMatrix = []

        rows = matrix_string.split('\n')
        #matrix = [[value for value in row] for row in line]
        matrix = [[int(value) for value in row.split(' ')] for row in matrix_string.split('\n')]
        print (matrix)

        for i in range(len(rows)):
            row = rows[i].split(' ')
            self.aMatrix.append(list(map(int, row)))

        print (self.aMatrix)

    def row(self, index):
        return [cell for cell in self.aMatrix[index-1]]

    def column(self, index):
        return [row[index-1] for row in self.aMatrix]

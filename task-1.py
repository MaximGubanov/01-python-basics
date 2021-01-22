class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        string = ''
        for line in self.matrix_list:
            string = string + f"{'   '.join(str(x) for x in line)}\n\n"
        return string

    def __add__(self, other):
        if len(self.matrix_list) == len(other.matrix_list):
            sum_matrix = []
            for num, line in enumerate(self.matrix_list):
                sum_matrix.append([x + other.matrix_list[num][num1] for num1, x in enumerate(line)])
            return sum_matrix
        else:
            print('Матрицы не совпадают')

matrix1 = Matrix([[12, 45, 21], [23, 24, 96], [17, 52, 80]])
matrix2 = Matrix([[13, 15, 27], [19, 64, 52], [89, 11, 55]])
matrix3 = Matrix(matrix1 + matrix2)
print(f'{matrix1}\n{matrix2}\nСумма элементов матрицы:\n{matrix3}')


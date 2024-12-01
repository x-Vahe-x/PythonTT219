import random

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.matrix)

    def __add__(self, other):
        if self.n != other.n or self.m != other.m:
            raise ValueError("Matrices must have the same dimensions to add.")
        result = Matrix(self.n, self.m)
        result.matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.m)] for i in range(self.n)]
        return result

    def __sub__(self, other):
        if self.n != other.n or self.m != other.m:
            raise ValueError("Matrices must have the same dimensions to subtract.")
        result = Matrix(self.n, self.m)
        result.matrix = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.m)] for i in range(self.n)]
        return result

    def __mul__(self, other):
        if self.m != other.n:
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix.")
        result = Matrix(self.n, other.m)
        result.matrix = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.m)) for j in range(other.m)] for i in range(self.n)]
        return result

    def calculate_mean(self):
        total_elements = self.n * self.m
        total_sum = sum(sum(row) for row in self.matrix)
        return total_sum / total_elements

    def sum_row(self, row_index):
        if 0 <= row_index < self.n:
            return sum(self.matrix[row_index])
        else:
            raise IndexError("Row index out of range.")

    def average_column(self, col_index):
        if 0 <= col_index < self.m:
            col_sum = sum(self.matrix[row][col_index] for row in range(self.n))
            return col_sum / self.n
        else:
            raise IndexError("Column index out of range.")

    def print_submatrix(self, col1, col2, row1, row2):
        if not (0 <= col1 <= col2 < self.m and 0 <= row1 <= row2 < self.n):
            raise IndexError("Submatrix indices are out of range.")
        
        for i in range(row1, row2 + 1):
            print(" ".join(map(str, self.matrix[i][col1:col2 + 1])))

if __name__ == "__main__":
    mat1 = Matrix(3, 3)
    mat2 = Matrix(3, 3)

    print("Matrix 1:")
    print(mat1.__str__())

    print("\nMatrix 2:")
    print(mat2.__str__())

    print("\nAddition of matrices:")
    print(mat1 + mat2)

    print("\nSubtraction of matrices:")
    print(mat1 - mat2)

    print("\nMultiplication of matrices:")
    mat3 = Matrix(3, 2) 
    print(mat1 * mat3)
import random

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]

    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(map(str, row)))

    def calculate_mean(self):
        total_elements = self.n * self.m
        total_sum = sum(sum(row) for row in self.matrix)
        return total_sum / total_elements

    def sum_row(self, row_index):
        if 0 <= row_index < self.n:
            return sum(self.matrix[row_index])
        else:
            raise IndexError("Row index out of range.")

    def average_row(self, row_index):
        if 0 <= row_index < self.n:
            return sum(self.matrix[row_index]) / self.m
        else:
            raise IndexError("Row index out of range.")

    def sum_column(self, col_index):
        if 0 <= col_index < self.m:
            return sum(self.matrix[row][col_index] for row in range(self.n))
        else:
            raise IndexError("Column index out of range.")

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
    mat = Matrix(4, 5)

    print("Original Matrix:")
    mat.print_matrix()

    print("\nMean of the matrix:", mat.calculate_mean())

    print("\nSum of row 2:", mat.sum_row(2))
    print("\nAverage of row 2:", mat.average_row(2))

    print("\nSum of column 3:", mat.sum_column(3))
    print("\nAverage of column 3:", mat.average_column(3))

    print("\nSubmatrix from [1, 3, 1, 2]:")
    mat.print_submatrix(1, 3, 1, 2)
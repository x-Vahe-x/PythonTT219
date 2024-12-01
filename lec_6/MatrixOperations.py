import random

def generate_random_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix

def get_column_sum(matrix, col_index):
    column_sum = 0
    for row in matrix:
        column_sum += row[col_index]
    return column_sum

def get_row_average(matrix, row_index):
    row = matrix[row_index]
    row_sum = sum(row)
    return row_sum / len(row)

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
    
matrix = generate_random_matrix(rows, cols)
    
print("Generated matrix:")
for row in matrix:
    print(row)
    
while True:
    col_index = int(input("Enter the column index for sum calculation: "))
    if 0 <= col_index < cols:
        column_sum = get_column_sum(matrix, col_index)
        print(f"Sum of column {col_index}: {column_sum}")
        break  
    else:
        print(f"Invalid column index. Please enter a value between 0 and {cols - 1}.")
    
while True:
    row_index = int(input("Enter the row index for average calculation: "))
    if 0 <= row_index < rows:
        row_avg = get_row_average(matrix, row_index)
        print(f"Average of row {row_index}: {row_avg}")
        break 
    else:
        print(f"Invalid row index. Please enter a value between 0 and {rows - 1}.")

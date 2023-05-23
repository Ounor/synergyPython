import random

matrix1 = []
for _ in range(10):
    row = [random.randint(-100, 100) for _ in range(10)]
    matrix1.append(row)

matrix2 = []
for _ in range(10):
    row = [random.randint(-100, 100) for _ in range(10)]
    matrix2.append(row)

matrix_sum = []
for i in range(10):
    row_sum = []
    for j in range(10):
        sum_value = matrix1[i][j] + matrix2[i][j]
        row_sum.append(sum_value)
    matrix_sum.append(row_sum)

print("Первая матрица:")
for row in matrix1:
    print(row)

print("Вторая матрица:")
for row in matrix2:
    print(row)

print("Сумма матриц:")
for row in matrix_sum:
    print(row)

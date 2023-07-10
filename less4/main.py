# Task 1
a = float(input("Введите длину прямоугольника: "))
b = float(input("Введите ширину прямоугольника: "))

area = a * b
perimeter = 2 * (a + b)

print("Площадь прямоугольника:", area)
print("Периметр прямоугольника:", perimeter)

# Task 2
number = int(input("Введите пятизначное целое число: "))

units = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
ten_thousands = (number // 10000) % 10

result = (tens ** units) * hundreds / (ten_thousands - thousands)

print(result)

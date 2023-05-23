# Task 1
a = float(input("Введите длину прямоугольника: "))
b = float(input("Введите ширину прямоугольника: "))

area = a * b
perimeter = 2 * (a + b)

print("Площадь прямоугольника:", area)
print("Периметр прямоугольника:", perimeter)

# Task 2
num = int(input("Введите пятизначное целое число: "))

units = num % 10
tens = (num // 10) % 10

exp = tens ** units

hundreds = (num // 100) % 10
result = exp * hundreds

thousands = (num // 1000) % 10
diff = tens * 10 + units - thousands * 1000

final_result = result / diff

print(final_result)

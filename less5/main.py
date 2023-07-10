# Task 1
num = int(input("Введите целое число: "))

if num == 0:
    print("нулевое число")
elif num > 0:
    if num % 2 == 0:
        print("положительное четное число")
    else:
        print("положительное нечетное число")
else:
    if num % 2 == 0:
        print("отрицательное четное число")
    else:
        print("отрицательное нечетное число")


# Task 2
word = input("Введите слово: ")

vowels = {"a", "e", "i", "o", "u"}
vowel_count = 0
consonant_count = 0

for letter in word:
    if letter in vowels:
        vowel_count += 1
    elif letter.isalpha():
        consonant_count += 1
    else:
        print(False)
        break

else:
    print("Количество гласных букв:", vowel_count)
    print("Количество согласных букв:", consonant_count)


# Task 3
X = int(input("Введите минимальную сумму инвестиций: "))
A = int(input("Введите сумму, которую готов вложить Майкл: "))
B = int(input("Введите сумму, которую готов вложить Иван: "))

if A >= X and B >= X:
    print(2)
elif A >= X:
    print("Mike")
elif B >= X:
    print("Ivan")
elif A + B >= X:
    print(1)
else:
    print(0)




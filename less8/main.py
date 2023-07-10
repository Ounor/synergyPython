#1
N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

reversed_numbers = numbers[::-1]
for num in reversed_numbers:
    print(num)
    
#2
def shift_array_right(arr):
    last_element = arr.pop()
    arr.insert(0, last_element)

arr = [1,2,3,4,5]

shift_array_right(arr)

#3

# Сколко кг переносит одна лодка
m = int(input())
# Кол-во рыбаков
n = int(input())

# Веса рыбаков
weights = []

for _ in range(n):
    weight = int(input())
    weights.append(weight)

weights.sort()

boats = 0
left = 0
right = n - 1

while left <= right:
    if weights[left] + weights[right] <= m:
        left += 1
    right -= 1
    boats += 1

print(boats)

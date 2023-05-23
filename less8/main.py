#1
N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

reversed_numbers = numbers[::-1]
for num in reversed_numbers:
    print(num)
    
#2
N = int(input())
array = list(map(int, input().split()))

reversed_array = array[::-1]
for num in reversed_array:
    print(num)
#3

m = int(input())
n = int(input())

weights = []
for _ in range(n):
    weights.append(int(input()))

weights.sort(reverse=True)

boats = 0
i = 0
while i < n:
    if weights[i] <= m:
        i += 1
    else:
        i += 2
    boats += 1

print(boats)

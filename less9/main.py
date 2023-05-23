#1
N = int(input())
numbers = list(map(int, input().split()))

unique_numbers = set(numbers)
count = len(unique_numbers)
print(count)

#2

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

set1 = set(list1)
set2 = set(list2)
common_numbers = set1.intersection(set2)
count = len(common_numbers)
print(count)

#3

numbers = list(map(int, input().split()))
seen_numbers = set()

for num in numbers:
    if num in seen_numbers:
        print("YES")
    else:
        print("NO")
        seen_numbers.add(num)

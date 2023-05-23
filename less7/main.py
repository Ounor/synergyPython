#1
string = input("Введите строку: ")

if string == string[::-1]:
    print("yes")
else:
    print("no")
    
#2
string = input("Введите строку: ")
new_string = " ".join(string.split())

print(new_string)

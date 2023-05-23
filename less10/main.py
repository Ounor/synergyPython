#1
pets = {}

name = input("Введите имя питомца: ")
species = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner = input("Введите имя владельца: ")

pets[name] = {
    'Вид питомца': species,
    'Возраст питомца': age,
    'Имя владельца': owner
}

age_text = "год" if age == 1 else "года" if 1 < age < 5 else "лет"

keys = list(pets[name].keys())
values = list(pets[name].values())

info = f"Это {values[keys.index('Вид питомца')]} по кличке \"{name}\". Возраст питомца: {values[keys.index('Возраст питомца')]} {age_text}. Имя владельца: {values[keys.index('Имя владельца')]}"
print(info)


#2

my_dict = {}

for i in range(10, -6, -1):
    my_dict[i] = i ** i

print(my_dict)

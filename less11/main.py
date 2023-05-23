#1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def factorial_list(n):
    result = []
    while n >= 1:
        result.append(factorial(n))
        n -= 1
    return result


input_number = 3
factorial_result = factorial(input_number)
factorial_list_result = factorial_list(factorial_result)
print("Факториал числа", input_number, ":", factorial_result)
print("Список факториалов от", factorial_result, "до 1:", factorial_list_result)


#2

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def create():
    new_id = len(pets) + 1

    name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")

    pets[new_id] = {
        name: {
            "Вид питомца": pet_type,
            "Возраст питомца": age,
            "Имя владельца": owner_name
        }
    }

    print("Запись успешно добавлена!")

def read():
    pet_id = int(input("Введите ID питомца: "))
    pet_info = get_pet(pet_id)

    if pet_info:
        pet_name, pet_data = next(iter(pet_info.items()))
        suffix = get_suffix(pet_data["Возраст питомца"])

        print(f'Это {pet_data["Вид питомца"]} по кличке "{pet_name}". '
              f'Возраст питомца: {pet_data["Возраст питомца"]} {suffix}. '
              f'Имя владельца: {pet_data["Имя владельца"]}')
    else:
        print("Питомец с указанным ID не найден.")

def update():
    pet_id = int(input("Введите ID питомца для обновления: "))
    pet_info = get_pet(pet_id)

    if pet_info:
        pet_name, pet_data = next(iter(pet_info.items()))

        print("Информация о питомце:")
        print(f'Вид питомца: {pet_data["Вид питомца"]}')
        print(f'Возраст питомца: {pet_data["Возраст питомца"]}')
        print(f'Имя владельца: {pet_data["Имя владельца"]}')

        new_name = input("Введите новое имя питомца (оставьте пустым, если не нужно менять): ")
        new_pet_type = input("Введите новый вид питомца (оставьте пустым, если не нужно менять): ")
        new_age = input("Введите новый возраст питомца (оставьте пустым, если не нужно менять): ")
        new_owner_name = input("Введите новое имя владельца (оставьте пустым, если не нужно менять): ")

        if new_name:
            pet_data["Вид питомца"] = new_pet_type
        if new_pet_type:
            pet_data["Вид питомца"] = new_pet_type
        if new_age:
            pet_data["Возраст питомца"] = int(new_age)
        if new_owner_name:
            pet_data["Имя владельца"] = new_owner_name

        print("Информация о питомце успешно обновлена!")
    else:
        print("Питомец с указанным ID не найден.")

def delete():
    pet_id = int(input("Введите ID питомца для удаления: "))
    pet_info = get_pet(pet_id)

    if pet_info:
        pet_name, _ = next(iter(pet_info.items()))
        del pets[pet_id]
        print(f"Питомец {pet_name} успешно удален!")
    else:
        print("Питомец с указанным ID не найден.")

def get_pet(ID):
    return pets.get(ID, False)

def get_suffix(age):
    last_digit = age % 10
    if age // 10 % 10 == 1:
        return "лет"
    elif last_digit == 1:
        return "год"
    elif 2 <= last_digit <= 4:
        return "года"
    else:
        return "лет"

def pets_list():
    print("Список питомцев:")
    for pet_id, pet_info in pets.items():
        pet_name, pet_data = next(iter(pet_info.items()))
        suffix = get_suffix(pet_data["Возраст питомца"])

        print(f'ID: {pet_id}')
        print(f'Имя питомца: {pet_name}')
        print(f'Вид питомца: {pet_data["Вид питомца"]}')
        print(f'Возраст питомца: {pet_data["Возраст питомца"]} {suffix}')
        print(f'Имя владельца: {pet_data["Имя владельца"]}')
        print()

# Главный цикл программы
command = ""
while command != "stop":
    command = input("Введите команду (create, read, update, delete, list, stop): ")

    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    elif command == "stop":
        print("Программа завершена.")
    else:
        print("Неверная команда. Попробуйте еще раз.")

import random

number = random.randint(1, 100)
# print(number)

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}

level = int(input("Введите уровень сложности от 1 до 3"))
max_count = levels[level]

while number != user_number:
    count += 1
    if count > max_count:
        print("LOOSER")
        break
    print(f"Попытка № {count}")
    user_number = int(input('Введите число'))
    if number < user_number:
        print("Ваше число больше загаданного")
    else:
        print("Ваше число меньше загаданного")
else:
    print("WIN!!!")

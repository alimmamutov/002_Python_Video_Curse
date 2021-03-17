# print('Hello')
# person_name = 'Max'
# print(type(person_name))
#
# age = int(input("your age:"))
# period = 3.2
# is_good = True
# person = None
#
# print(person_name, age, sep='//')
# print(person_name,end="")
# print(age, end="/")

# name = input('What is your name? ')
# print('Hi', name)

# if age < 18:
#     print("Allow")
#     print("ggg")
# elif age==25:
#     print("25")
#     print()
# else:
#     print( "NOOO" )
#     if 2 < 3 :
#         print("dbd")
#         print("sfs")
# number = 0
#
# while number < 100:
#     if number % 2 == 0:
#         print(number, end=" ")
#
#     number += 1

# # 1
# print('Задание 1')
# number = float(input('Введите любое число:\n'))
# print(number + 2)

# # 2
# print('Задание 2')
#
# while True:
#     number = int(input('Введите любое число от 1 до 9:\n'))
#     if 0 < number < 10:
#         break
#     print("Вы ввели неправильное число")
#
# print(number**2)

# 2

name = str(input("Name: "))
surname = str(input("Surname: "))
age = int(input("Age: "))
weight = int(input("Weight: "))

if age < 30:
    if 50 <= weight < 120:
        print("Good")
    else:
        print("Not good")

elif 30 <= age < 40:
    if 50 <= weight < 120:
        print("Good")
    else:
        print("Not good!!!")
else:
    if 50 <= weight < 120:
        print("Good")
    else:
        print("You will die!!!")

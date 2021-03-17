name = "Alim Mamutov"
age = 27
# print(name[-1])

# print(name[:3])
# print(len(name))
# print(name.find('la'))
# print(name.split(' '))

# hello_str = 'Привет, %s, тебе %d лет' % (name, age)
# print(hello_str)
#
# hello_str = 'Привет, {}, тебе {} лет'.format(name, age)
# print(hello_str)

# top5 = 'Первые 5 мест на соревнованиях: 1. Иванов 2. Петров 3. Сидоров 4. Орлов 5. Соколов'
# # Поздравляем 1. ИВАНОВ 2. ПЕТРОВ 3 СИДОРОВ с успехом!
#
# start = top5.find('1')
# end = top5.find('4')
#
# top3 = top5[start:end]
#
# result = "Поздравляем {} с успехом!".format(top3.upper())
#
# print(result)

# friends = ['Max', 'Leo', 'Kate']
#
# print(friends)
#
# friends.append('Ron')
#
# print(friends)
#
# print(friends.pop())
#
# print(friends)

# print('СОРЕВНОВАНИЯ ПО PYTHON')
# count = int(input('Введите количество участников: '))
# i = count
# members = []
# while i > 0:
#     name = input('Кто занял {} место?'.format(i))
#     members.append(name)
#     i -= 1
#
# # кто участвовал в соревновании (По алфавиту)
# print('В соревновании участвовали: ',sorted(members))
#
# # Мы записали людей с конца?
# members.reverse()
#
# # Нам нужно взять первые 3 места
# result = members[:3]
# result = 'Победители: {}. Поздравляем!'.format(result)
# print(result)

# # for
#
# friends = ['Max', 'Leo', 'Kate']
# friendName = 'Max'
# roles = ('user', 'manager', 'admin')
#
# for friend in friends:
#     print(friend)
#
# for letter in friendName:
#     print(letter)
#
# for role in roles:
#     print(role)

# numbers = range(10)
# print(numbers)
# print(type(numbers))
# print(list(numbers))

# friends = ['Max', 'Leo', 'Kate']
#
# for i in range(len(friends)):
#     # print(i)
#     print(friends[i])
#

# for number in range(1,1000,2):
#     print(number)

# friend = {
#     'name': 'Max',
#     'age': 23
# }

# max_things = {'Телефон', "Шорты", "Рубашка", "Бритва"}
# kate_things = {"Телефон", "Шорты", "Зонт", "Помада"}
#
# print(max_things | kate_things)
# print(max_things & kate_things)
# print(max_things - kate_things)
# print(kate_things - max_things)

# #1: Даны два произвольные списка.
# # Удалите из первого списка элементы присутствующие во втором списке.
#
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]
# my_set = set(my_list_1)-set(my_list_2)
# my_list = list(my_set)
# my_list.sort()
# print(my_set)
# print(my_list)

#   2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
#   Ваша задача — вывести дату в текстовом виде, например: второе ноября 2013 года.
#   Склонением пренебречь (2000 года, 2010 года)

mas = []
for firstDigit in range(0, 4):
    for secondDigit in range(0, 10):
        val = str(firstDigit)+str(secondDigit)
        mas.append(val)

        if len(mas) == 32:
            break

print(mas)
print(len(mas))
# my_date = input("Введите дату в формате dd.mm.yyyy")
for my_date in mas:

    date_1 = ("", "", "Двадцать", "Тридцать", "Сорок", "Пятьдесят", "Шестьдесят", "Семьдесят", "Восемьдесят", "Девяносто",
              "Десятое", "Одиннадцатое", "Двенадцатое", "Тринадцатое", "Четырнадцатое", "Пятнадцатое","Шестнадцатое","Семнадцатое","Восемнадцатое","Девятнадцатое",
              "Двадцатое")

    date_2 = ("","Первое", "Второе", "Третье", "Четвертое", "Пятое","Шестое", "Седьмое", "Восьмое", "Девятое",
              "Десятое", "Двадцатое", "Тридцатое")


    dateList = my_date.split('.')
    print(f'{my_date},{dateList}')

    # Работа с датой
    userDate = dateList[0]

    if userDate[0] == '0':
        print(date_2[int(userDate[1])])
    elif userDate[0] == '1':
        digit = int(userDate)
        print(date_1[digit])
    elif userDate[1] == '0':
        digit = 9+int(userDate[0])
        print(date_2[digit])
    else: #Составное
        digit1 = int(userDate[0])
        digit2 = int(userDate[1])
        print(date_1[digit1],date_2[digit2])

result = f''

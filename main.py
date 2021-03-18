# функция enumerate

# winners = ['Leo', 'Max', 'Kate']
# en = enumerate(winners, 1)
# for number, winner in enumerate(winners, 1):
#     print(number, winner)

# def print_sep():
#     print('=' * 100)
#
# print_sep()

# Функция в качестве параметра

def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]


def is_even(number):
    return number % 2 == 0


def is_not_even(number):
    return number % 2 != 0


print(my_filter(numbers, is_even))
print(my_filter(numbers, is_not_even))

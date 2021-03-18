from random import randint, choice, sample, shuffle
# # импорт определенных функций из библиотеки

# import math
#
# r = 100
#
# print(2*r*math.pi)
# print(math.pow(r,2)*math.pi)

players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
print(choice(players))
print(sample(players,3))
cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
print(cards)
shuffle(cards)
print(cards)


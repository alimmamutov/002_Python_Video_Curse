
# 3: Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения: name - строка полученная от пользователя, health = 100, damage = 50. ###
# Поэкспериментируйте с значениями урона и жизней по желанию.
#  Теперь надо создать функцию attack(person1,person2). Примечание: имена аргументов можете указать свои.
#  Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от
# health атакуемого. Функция должна сама работать со словарями и изменять их значения.
#
# 4: Давайте усложним предыдущее
# задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа) Теперь надо добавить
# новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor Следовательно,
# у вас должно быть 2 функции: Наносит урон. Это улучшенная версия функции из задачи 3. Вычисляет урон по отношению к
# броне.
#
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья
# персонажа.

playerName = input('Input player name: ')
# playerHealth = int(input('Input player health: '))
# playerDamage = int(input('Input player damage: '))

enemyName = input('Input enemy name: ')
# enemyHealth = int(input('Input enemy health: '))
# enemyDamage = int(input('Input enemy damage: '))

player = {'name': playerName,
          'health': 100,
          'damage': 50,
          'armor': 1.2}
enemy = {'name': enemyName,
         'health': 50,
         'damage': 30,
         'armor': 1}


def attack(unit, target):
    damage = get_damage(unit['damage'], target['armor'])
    target['health'] -= damage


def get_damage(damage, armor):
    return damage/armor


print(player)
print(enemy)

attack(enemy, player)

print(player)
print(enemy)

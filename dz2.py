#Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
#Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
#определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от
#1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

from itertools import combinations
import random
def if_safe(arrangement):
    for queen1, queen2 in combinations(arrangement, 2):
        #  на одной вертикали или горизонтали
        if queen1[0] == queen2[0] or queen1[1] == queen2[1]:
            return False

        # на одной диагонали
        if abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1]):
            return False

    return True


# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
def gen_combination():
    # Генерируем случайную расстановку ферзей
    queens = [(i, random.randint(1, 8)) for i in range(1, 9)]
    return queens

def get_combinations():
    true_combinations = []
    counter = 4
    while counter > 0:
        queens = gen_combination()
        if if_safe(queens) and  queens not in true_combinations:
            true_combinations.append(queens)
            counter -= 1    

# Выводим успешные расстановки ферзей
    for num, coord in enumerate(true_combinations):
        print(f"Успешная расстановка {num+1}: {coord}")
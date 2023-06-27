from .dz2 import if_safe, get_combinations


queens = [(1, 2), (1, 3), (8, 6), (7, 5), (5, 2), (3, 3), (7, 5), (6, 6)]

valid = if_safe(queens) 

if valid:
    print("Нет пары бьющих друг друга")
else:
    print("Есть пара бьющих друг друга ферзей")

get_combinations()    
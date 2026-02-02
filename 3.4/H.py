""""
В детском саду ежедневно подают новую кашу на завтрак.
Напишите программу, которая строит расписание каш на ближайшие дни на основе заданного меню.

Формат ввода
Вводится натуральное число 
M
M — количество каш в меню.
В каждой из последующих 
M
M строк записано одно название каши.
В конце передается натуральное число 
N
N — количество дней.

Формат вывода
Вывести список каш в порядке подачи.
"""
from itertools import cycle
m = int(input())
dish_list = []
for _ in range(m):
    dish_list.append(input())
menu_list = []
n = int(input())
for dish in cycle(dish_list):
    if len(menu_list) == n:
        break
    menu_list.append(dish)
print('\n'.join(menu_list))
"""
Теперь выражения могут содержать переменное количество переменных, обозначенных заглавными латинскими буквами.

Напишите программу, которая строит таблицу истинности для заданного логического выражения.

Формат ввода
Вводится логическое выражение от нескольких переменных валидное для языка Python. Все переменные заданы заглавными латинскими буквами.

Формат вывода
Выведите таблицу истинности данного выражения.
"""
from itertools import product
condition = input()
var_list = []
for char in condition:
    if char.isupper():
        var_list.append(char)
var_list = sorted(set(var_list))
values = list(product([0, 1], repeat=len(var_list)))
print(" ".join(var_list) + " F")
for value in values:
    var_dict = dict(zip(var_list, value))
    if eval(condition, {}, var_dict):
        f = 1
    else:
        f = 0
    print(" ".join(map(str, value)) + " " + str(f))
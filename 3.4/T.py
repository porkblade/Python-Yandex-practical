"""
На этот раз придётся справиться с выражением, в котором встречаются нестандартные логические операции: импликация, строгая дизъюнкция и эквивалентность.
Они не поддерживаются в Python напрямую, но вы сможете реализовать их самостоятельно.

Напишите программу, которая для заданного логического выражения строит таблицу истинности, включая поддержку следующих операций:

-> — импликация
^ — строгая дизъюнкция
~ — эквивалентность
Формат ввода
Вводится логическое выражение от нескольких переменных.

Возможное содержание выражения:

Заглавная латинская буква — переменная;
not — отрицание;
and — конъюнкция;
or — дизъюнкция;
^ — строгая дизъюнкция;
-> — импликация;
~ — эквивалентность;
() — логические скобки.
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
    i = 0
    new_condition = ""
    while i < len(condition):
        if condition[i].isupper():
            for j in range(len(var_list)):
                if var_list[j] == condition[i]:
                    new_condition += value[j]
                    break
            i += 1
        elif condition[i:i + 2] == "->":
            new_condition += "<="
            i += 2
        elif condition[i] == "~":
            new_condition += "=="
            i += 1
        elif condition[i] == "^":
            new_condition += "!="
            i += 1
        else:
            new_condition += condition[i]
            i += 1
    if eval(new_condition):
        f = 1
    else:
        f = 0
    print(" ".join(map(str, value)) + " " + str(f))
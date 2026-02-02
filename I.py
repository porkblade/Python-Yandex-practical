""""
Местная фабрика канцелярских товаров заказала программу, которая генерирует таблицы умножения.
Давайте поможем производителю.

Напишите программу, которая выводит таблицу умножения размером N×N — построчно, по одному ряду на строку.

Формат ввода
Вводится одно натуральное число — требуемый размер таблицы.

Формат вывода
Таблица умножения заданного размера.
"""
from itertools import product
n = int(input())
number_list = []
for i in range(1, n + 1):
    number_list.append(i)
number_pair_comb = list(product(number_list, repeat=2))
count = 0
string = ''
for number_pair in number_pair_comb:
    number = number_pair[0] * number_pair[1]
    if count < n - 1:
        count += 1
        string += str(number) + ' '
    else:
        count = 0
        string += str(number) + '\n'
print(string)
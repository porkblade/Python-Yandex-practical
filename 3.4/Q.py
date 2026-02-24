"""
Давайте вновь поможем Виталию — теперь его интересует, какой вариант расклада идёт сразу после уже полученного.
Напишите программу, которая находит следующий подходящий вариант тройки карт, соответствующий условиям.

Формат ввода
В первой строке записана масть, которая должна присутствовать в тройке.
Во второй строке записан достоинство, которого не должно быть в тройке.
В третьей строке записан предыдущий вариант полученный Виталием.

Формат вывода
Выведите следующий вариант расклада.
"""
from itertools import combinations
from itertools import product
key = input()
nom_rem = input()
n_var = input()
nom = ["10", "2", "3", "4", "5", "6", "7", "8", "9", "валет", "дама", "король", "туз"]
suit_dict = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
nom.remove(nom_rem)
suit_list = list(suit_dict.values())
deck = list(product(sorted(nom), sorted(suit_list)))
d_c = list(combinations(deck, 3))
n_list = []
s = ""
for i in range(len(d_c)):
    if suit_dict[key] == d_c[i][0][1] or suit_dict[key] == d_c[i][1][1] or suit_dict[key] == d_c[i][2][1]:
        s = d_c[i][0][0] + " " + d_c[i][0][1] + ", " + d_c[i][1][0] + " " + d_c[i][1][1] + ", " + d_c[i][2][0] + " " + d_c[i][2][1]
        n_list.append(s)
for i in range(len(n_list)):
    if n_list[i] == n_var:
        print(n_list[i + 1])
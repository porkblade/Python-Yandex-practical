""""
Ребята в классе решили устроить чемпионат по шашкам по принципу «каждый с каждым».
Напишите программу, которая составляет список всех возможных игр между учениками.

Формат ввода
В первой строке записано число учеников (
N
N).
В каждой из последующих 
N
N строк записано одно имя.

Формат вывода
Список игр в формате:
<Игрок 1> - <Игрок 2>
Порядок игр не имеет значения.
"""
from itertools import combinations
n = int(input())
participant_list = []
for _ in range(n):
    participant_list.append(input())
pair_list = list(combinations(participant_list, 2))
for pair in pair_list:
    print(f"{pair[0]} - {pair[1]}")
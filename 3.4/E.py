full_list = []
for _ in range(3):
    list_part = input().split(', ')
    for item in list_part:
        full_list.append(item)
for index, value in enumerate(sorted(full_list), 1):
    print(f'{index}. {value} ')
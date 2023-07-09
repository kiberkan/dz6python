import random
print(list_1 := [random.randint(1,10) for i in range(20)])
min_number = int(input('минимальный элемент: '))
max_number = int(input('максимальный элемент: '))
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i, end= ' ')
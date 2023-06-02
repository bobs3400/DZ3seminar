num_1 = int(input("Введите количество элементов в первом массиве: "))
num_2 = int(input("Введите количество элементов во втором массиве: "))
list_1 = []
list_2 = []
list_3 = []
print('Введите первый список')
for i in range(num_1):
    list_1.append(int(input()))
print('Введите второй список')
for i in range(num_2):
    list_2.append(int(input()))
for i in range(num_1):
    for j in range(num_2):
        if list_1[i] == list_2[j]:
            list_3.append(list_1[i])
list_3.sort()
print(list_3)        

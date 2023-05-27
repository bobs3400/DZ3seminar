from random import randint
number = int(input("Введите длину списка: "))
num_x = int(input("Введите искомое число: "))
my_list = []
min_razn = 10
for i in range(number):
    my_list.append(randint(0, 10))
    if abs(my_list[i] - num_x) < min_razn:
        min_razn = abs(my_list[i] - num_x)
        count = i
print(*my_list)
print(num_x)
print(my_list[count])
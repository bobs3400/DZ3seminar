from random import randint
number = int(input("Введите длину списка: "))
num_x = int(input("Введите искомое число: "))
my_list = []
count = 0
for i in range(number):
    my_list.append(randint(0, 10))
    if my_list[i] == num_x:
        count += 1
print(*my_list)
print(num_x)
print(count)
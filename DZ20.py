list_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
list_2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
list_3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
list_4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
list_5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
list_8 = ['J', 'X', 'Ш', 'Э', 'Ю']
list_10 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']
new_word = input("Введите слово: ")
new_word = new_word.upper()
print(new_word)
summ = 0
for i in range(len(new_word)):
    if list_1.count(new_word[i]) > 0:
        summ = summ + 1
    elif list_2.count(new_word[i]) > 0:
        summ = summ + 2
    elif list_3.count(new_word[i]) > 0:
        summ = summ + 3
    elif list_4.count(new_word[i]) > 0:
        summ = summ + 4
    elif list_5.count(new_word[i]) > 0:
        summ = summ + 5
    elif list_8.count(new_word[i]) > 0:
        summ = summ + 8
    elif list_10.count(new_word[i]) > 0:
        summ = summ + 10
print(summ)
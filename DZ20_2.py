list_1 = {'AEIOULNSTRАВЕИНОРСТ': 1,
        'DGДКЛМПУ': 2,
        'BCMPБГЁЬЯ': 3,
        'FHVWYЙЫ': 4,
        'KЖЗХЦЧ': 5,
        'JXШЭЮ': 8,
        'QZФЩЪ': 10}
new_word = input("Введите слово: ")
new_word = new_word.upper()
print(new_word)
summ = 0
for key in list_1:
    for i in range(len(new_word)):
        if key.__contains__(new_word[i]):
            summ = summ + list_1.get(key) 
print(summ)        
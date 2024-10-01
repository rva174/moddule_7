""" 9_3_ Генераторные сборки
"""

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(i[0]) - len(i[1]) for i in zip(first, second) if (len(i[0]) != len(i[1])))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))

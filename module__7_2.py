def custom_write(file_name, strings):
    file_name = 'test.txt'
    strings_positional = {}
    file = open('test.txt', 'a', encoding='utf-8')

    for i, j in enumerate(strings):
        key = (i+1, file.tell())
        strings_positional[key] = j
        file.write(j + '\n')
    file.close()

    return strings_positional

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)




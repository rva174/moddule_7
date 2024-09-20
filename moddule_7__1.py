def custom_write(file_name, string:list):
    file_name = test.txt
    string = []
 #   string = info


    file = open(file_name, 'w', encoding='utf-8')

    file.write(info)
    content = string
    file.close()
    return result




string = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

# {{1, 0}: 'Text for tell', (2, 16): 'Исподьзуйте кодировку utf-8'}
# Где:
# 1, 2 -  номера записанных строк.
# 0, 16 - номера байт, на которых началась запись строк.
# 'Text for tell', 'Исподьзуйте кодировку utf-8'- сами строки

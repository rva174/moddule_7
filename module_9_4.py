# 9_4_ Создание функций на лету _Функциональное многообразие

# Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda f, s: f == s, first, second)))

# Замыкание
from random import choice

class MysticBall:
    words = []

    def __init__(self, *args):
        self.words = args

    def __call__(self):
        return choice(self.words)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for i in data_set:
                file.write(str(i))
    return write_everything
    print(write_everything)


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())


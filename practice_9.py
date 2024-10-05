# Первое задание достаточно большое. Оно включает в себя три подпункта (Рис.1):
# 1. Написать функцию, которая возвращает другую функцию, повторения двух символов «n» раз.
# У нас есть какая-то строчка, и нам нужно написать функцию, которая будет возвращать повторение
# первых двух символов. Но это не просто функция, это функция, которая будет генерировать
# другие функции, которые будут повторять первые два символа «n» количество раз.
# 2. Создать массив функций с различными параметрами «n» и применить все эти функции поочерёдно
# к аргументу «animal».
# 3. Применить все функции, которые мы до этого создадим, поочерёдно к массиву аргументов.

animal = 'мишка'
animals = ['зайка', 'мишка', 'бегемотик']

# 1
def gen_repeat(n):
    def repeat(animals):
        return(animals[:2] + '-') * n + animal
    return repeat

test_1 = gen_repeat(1)
test_2 = gen_repeat(2)

print(test_1(animal))
print(test_2(animal))

# 2
repetitions = [gen_repeat(n) for n in range(1, 4)]
print(repetitions)

result = [func(animal) for func in repetitions]
print(result)

# 3
def memoize_func(f):
    mem = {}

    def wrapper(*args):
        print(f'Выполнение функции с аргументами={args}, внутренняя память={mem}')
        if args not in mem:
            mem[args] = f(*args)
            return f'Функция выполнилась, ответ = {mem[args]}'
        else:
           return f'Функция уже была выполнена раньше, ответ = {mem[args]}'
    return wrapper

@memoize_func
def func(a, b):
    print(f'Выполняем функцию с аргументами ({a}, {b})')
    return a ** b

print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 2), '\n')
print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')
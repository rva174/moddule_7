
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы- {i}')
    return result, incorrect_data
def calculate_average(numbers):
    try:
        sum , incorrect_data = personal_sum(numbers)

        if len(numbers) - incorrect_data == 0:
            raise ZeroDivisionError

        return  sum / (len(numbers) - incorrect_data)

    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return None



# Строка перебирается,но каждый символ- строковый тип
print(f'Результат 1: {calculate_average('1, 2, 3')}')
# Учитываются только 1 и 3
print(f'Результат 2: {calculate_average([1, 'Строка', 3, 'Еще строка'])}')
# Передана не коллекция
print(f'Результат 3: {calculate_average(567)}')
# Все должно работать
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
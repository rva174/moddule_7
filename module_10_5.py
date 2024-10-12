#10_5 Многопроцессорное программирование

from datetime import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []
    print(f'Открытие файла {name} для записи построчно в список all-data')
    with open(name, 'r') as file:
        while True:
            line = file.readline()
 #           print(line)
            all_data.append(line)
            if not line:
                break
        print(f'Запись строк файла {name} в список all-data завершена')
    file.close

#    print(all_data)

# Линейный вызов
# filenames = [f'file {number}.txt' for number in range(1,5)]
# start_time = datetime.now()
# for file in filenames:
#     read_info(file)
#
# total_time = datetime.now() - start_time
# print('Запись файлов построчно в список завершена')
# print(f'total_time: {total_time}')


if __name__ == '__main__':
    filenames = [f'file {number}.txt' for number in range(1,5)]

    start_time = datetime.now()
    with Pool(4) as pool:
        pool.map(read_info, filenames)

    total_time = datetime.now() - start_time
    print('Запись файлов построчно в список завершена')
    print(f'total_time: {total_time}')



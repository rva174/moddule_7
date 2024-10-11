#10_5 Многопроцессорное программирование

from datetime import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []

    print(f'Открытие файла {name} для записи построчно в список all-data')
    with open(name, 'r') as file:

        while True:
            line = file.readline()
            all_data.append(line)

            if not line:
                break
        print(f'Запись строк файла {name} в список all-data завершена')
    file.close

# # Линейный вызов
# filenames = [f'file {number}.txt' for number in range(1,5)]
# start_time = datetime.now()
# start = datetime.now()
# for file in filenames:
#     read_info(file)
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



 # #  file = open("name", "r")
 #   for name in filenames(len(filenames)):
 #       while True:
 #       # считываем строку
 #
 #       # прерываем цикл, если строка пустая
 #       #    print(line)
 #           all_data.append(line + '\n')
 #       #    print(all_data)
 #           if not line:
 #               break
 #       # выводим строку
 #   #   print(line.strip())
 #
 #   print(all_data)
 #
 #   filenames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
 #   print(filenames)
 #
 #   for name in filenames(len(filenames)):
 #      with open('name', 'r') as file:
 #
 #          file1 = open("file 1.txt", "r")
 #
 #          while True:
 #              # считываем строку
 #              line = file1.readline()
 #              # прерываем цикл, если строка пустая
 #              if not line:
 #                  break
 #              # выводим строку
 #              print(line.strip())
 #
 #          # закрываем файл
 #          file.close
 #





         # while True:
         #     # считываем строку
         #     all_data = [line for line in file]
         # print(all_data)

# строка пустая
#
#filenames = [f'file {number}.txt' for number in range(1,5)]
# print(filenames)
#print(all_data)


# закрываем файл







#print([all_data])
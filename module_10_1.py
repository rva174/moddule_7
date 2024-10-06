#10_1 Создание потоков
from threading import Thread
from datetime import datetime
from time import sleep

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            with open(file_name, 'a', encoding='utf-8') as file:
                file.write(f'Какоe-то слово № {i+1}' + '\n')
                sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

start_time = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
total_time = datetime.now() - start_time
print(f'Paбота потоков {total_time}')

thr5 = Thread(target=write_words, args=(10, 'example5.txt'))
thr6 = Thread(target=write_words, args=(30, 'example6.txt'))
thr7 = Thread(target=write_words, args=(200, 'example7.txt'))
thr8 = Thread(target=write_words, args=(100, 'example8.txt'))

start_time = datetime.now()
thr5.start()
thr6.start()
thr7.start()
thr8.start()

thr5.join()
thr6.join()
thr7.join()
thr8.join()
total_time = datetime.now() - start_time
print(f'Paбота потоков {total_time}')
import random
import time
from threading import Thread
import queue

class Bulka(Thread):
    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        while True:
 #           time.sleep(random.randint(1, 2))
            time.sleep(3)
 #           if random.random() > 0.9:
            if random.random() > 0.5:

                self.queue.put('Подгорелая булка')
            else:
                self.queue.put('Нормальная булка')

class Kotleta(Thread):
    def __init__(self, queue, count):
        self.queue = queue
        self.count = count
        super().__init__()

    def run(self):
        while self.count:
            print(self.queue.qsize())
#            bulka = self.queue.get()
            bulka = self.queue.get(timeout=5)
            if bulka == 'Нормальная булка':
 #               time.sleep(random.randint(1, 2))
                time.sleep(1)
                self.count -= 1
#            print(f'Булок к приготовлению осталось: {self.count}')
            print('Булок к приготовлению осталось ', self.count)

#queue = queue.Queue(maxsize=10)
queue = queue.Queue()

t1 = Bulka(queue)
t2 = Kotleta(queue, 20)

t1.start()
t2.start()

t1.join()
t2.join()

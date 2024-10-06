#10_2 Потоки на классах
from threading import Thread
from time import sleep
class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f'{self.name}, на нас напали!')

        days = 0
        while self.enemies > 0:
            sleep(1)
            days += 1
            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0
            print(f'{self.name} сражается {days} суток, осталось {self.enemies} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней.')


#def main():
first_knight = Knight('Bors', 10)
second_knight = Knight('Lamorak', 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')


# first_knight = Thread(target=first_name, args=first_power)
# second_knight = Thread(target=name, args=power)

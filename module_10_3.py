#10.3 Блокировки и обработка ошибок

import threading
from random import randint
from time import sleep

class Bank:
    lock = threading.Lock()
    def __init__(self):
        self.balance = 0

    def deposit(self):
        for i in range(100):
            plus = randint(50, 500)
            print(f'Запрос на {plus}')
            self.balance += plus
            print(f'Пополнение: {plus}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            minus = randint(50, 500)
            print(f'Запрос на {minus}')
            if minus <= self.balance:
                self.balance -= minus
                print(f'Снятие: {minus}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
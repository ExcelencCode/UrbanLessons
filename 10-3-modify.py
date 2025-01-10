import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0  # Начальный баланс
        self.lock = threading.Lock()  # Объект для блокировки потоков

    def deposit(self):
        for _ in range(100):  # 100 транзакций пополнения
            deposit_amount = random.randint(50, 500)
            with self.lock:  # Защищаем доступ к балансу
                self.balance += deposit_amount
                print(f"Пополнение: {deposit_amount}. Баланс: {self.balance}")
            time.sleep(0.001)  # Имитация времени пополнения

    def take(self):
        for _ in range(100):  # 100 транзакций снятия
            with self.lock:  # Защищаем доступ к балансу
                take_amount = random.randint(50, 500)
                print(f'Запрос на {take_amount}. ', end='')
                if take_amount > self.balance:
                    print("Запрос отклонён, недостаточно средств")
                else:
                    self.balance -= take_amount
                    print(f"Снятие: {take_amount}. Баланс: {self.balance}")

            time.sleep(0.001)  # Имитация времени снятия


# Создание объекта банка
bk = Bank()

# Создание потоков для выполнения методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Вывод итогового баланса
print(f'Итоговый баланс: {bk.balance}')

import random
import time
import threading
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number  # Номер стола
        self.guest = None  # Гость за столом

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name  # Имя гостя

    def run(self):
        # Гость задерживается случайное количество времени от 3 до 10 секунд
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # Очередь для гостей, которые ждут
        self.tables = tables  # Список столов кафе

    def guest_arrival(self, *guests):
        for guest in guests:
            # Ищем свободный стол
            free_table = None
            for table in self.tables:
                if table.guest is None:
                    free_table = table
                    break

            if free_table:  # Если нашли свободный стол
                free_table.guest = guest  # Сажаем гостя за стол
                guest.start()  # Запускаем поток гостя
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:  # Если нет свободных столов, то добавляем в очередь
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        # Обслуживаем гостей пока очередь не пуста или хотя бы один стол занят
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():  # Если гость завершил приём пищи
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаем стол

                    if not self.queue.empty():  # Если очередь не пуста, сажаем следующего гостя
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

            time.sleep(1)

# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Rakhmatullo', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()

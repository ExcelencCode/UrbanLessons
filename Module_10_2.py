import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self, day=0, enemies=100):
        print(f'{self.name}, на нас напали!')
        while enemies>0:
            time.sleep(1)
            day += 1
            enemies -= self.power
            print(f'\n{self.name} сражается {day}-й день. ', end='')
            # А это чтобы число врагов не становилось отрицательным при богатырской силе рыцаря
            if enemies > 0:
                print(f'Осталось {enemies} врагов...')
            else:
                print('Врагов не осталось ваще.')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 53)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

# Ждём окончания всех потоков. А то все битвы заканчиваются раньше докладов с поля боя...
first_knight.join()
second_knight.join()

print('\nВсе битвы закончились!')


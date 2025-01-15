import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as f: # Открываем файл name для чтения
        while True:
            line = f.readline()  # Считываем строку
            if not line:  # Если строка пустая (конец файла)
                break     # Прерываем цикл
            all_data.append(line.strip())  # Добавляем строку в список без переноса строки


if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]  # Создаём список имён файлов

    # Линейный способ

    start_time = time.perf_counter() # Засекаем время начала

    for filename in filenames:  # Вызываем функцию поочерёдно для каждого файла из списка
        read_info(filename)

    linear_time = time.perf_counter() - start_time # Вычисляем время выполнения

    print(f"Время линейного выполнения: {linear_time:.2f} секунд") # Выводим результат

    # Многопроцессный способ

    start_time = time.perf_counter() # Засекаем время начала

    with Pool() as pool: # Создаём пул процессов
        pool.map(read_info, filenames) # вызывая функцию для каждого файла

    parallel_time = time.perf_counter() - start_time  # Вычисляем время выполнения

    print(f"Общее время многопроцессного выполнения: {parallel_time:.2f} секунд")
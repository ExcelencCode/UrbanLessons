import time
import threading
from time import sleep


# Функция для записи слов в файл с задержкой
def write_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'a') as f:
            f.write(f"Какое-то слово № {i}\n")
        sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Главная часть программы
if __name__ == "__main__":
    # 1. Последовательное выполнение
    start_time = time.time()
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")
    end_time = time.time()
    print(f"Работа последовательных вызовов: {end_time - start_time:.3f} секунд")

    # 2. Многозадачность с использованием потоков
    start_time = time.time() # Отмечаем начало выполнения

    # Создаем потоки
    threads = [
        threading.Thread(target=write_words, args=(10, "example5.txt")),
        threading.Thread(target=write_words, args=(30, "example6.txt")),
        threading.Thread(target=write_words, args=(200, "example7.txt")),
        threading.Thread(target=write_words, args=(100, "example8.txt"))
    ]

    # Запуск всех потоков
    for thread in threads:
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Работа потоков: {end_time - start_time:.3f} секунд")

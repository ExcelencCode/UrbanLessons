first = 'Мама мыла раму'
second = 'Рамена мало было'

rr = list(map(lambda f, s: f == s, first, second))
print(rr)

# Замыкание:
def get_advanced_writer(file_name):
    # Вложенная функция для записи данных в файл
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for item in data_set:
                file.write(str(item) + '\n')

    return write_everything

# Создаем функцию для записи в файл example.txt
write = get_advanced_writer('example.txt')

# Записываем различные данные в файл
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__
from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        # Возвращаем случайное слово из списка words
        return choice(self.words)


# Создаем объект MysticBall с набором слов
first_ball = MysticBall('Да', 'Нет', 'Наверное')

# Вызываем объект как функцию, чтобы получить случайный ответ
print(first_ball())
print(first_ball())
print(first_ball())

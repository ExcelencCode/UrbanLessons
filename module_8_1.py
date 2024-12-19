def add_everything_up(a, b):
    try:
        result = a+b
        print(result)
    except TypeError as exc:
        print(f'Произошла ошибка "{exc}".\n'
              f'Введены данные, которые нельзя сложить.\n'
              f'{a}{b}')
        return ''
    else:
        print('Всё в порядке')
        return ''
    finally:
        print('Конец фильмы')
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
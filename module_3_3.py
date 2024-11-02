# Функция с параметрами по умолчанию
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params('bla', 2, 45.28)
print_params('bla', c=33.3)
print_params(7)
print_params(b = 25)
print_params(c = [1,2,3])

# Распаковка параметров
values_list = ['stroka', ['q', 2, 3.8], 66]
values_dict = {'a' : 17, 'b' : 'zhuzha', 'c' : False}
print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры
values_list_2 = [2, 'ru-ru']
print_params(*values_list_2, 42)


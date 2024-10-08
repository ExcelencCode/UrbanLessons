my_dict = dict(Andy=1975, Boris=1990, Ivan=2005, Igor=1961)
print(my_dict)
print(my_dict['Ivan']) # Вывод значения по существующему ключу
print(my_dict.get('Ktokto', 'Такого ключа нет в словаре')) # Попытка обращения к отсутствующему ключу
my_dict.update({'dusya': 2005, 'musya': 2010}) # Добавление двух пар
print(my_dict.pop('Boris')) # Удаление ключа и вывод его значения на экран
print(my_dict)
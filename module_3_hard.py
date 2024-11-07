data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data):
    total_sum = 0

    # Если data - это число, добавляем его к общей сумме
    if isinstance(data, (int, float)):
        total_sum += data

    # Если data - это строка, добавляем её длину
    elif isinstance(data, str):
        total_sum += len(data)

    # Если data - список, кортеж или множество, обрабатываем его элементы рекурсивно
    elif isinstance(data, (list, tuple, set)):
        for i in data:
            total_sum += calculate_structure_sum(i)

    # Если data - словарь, обрабатываем его ключи и значения
    elif isinstance(data, dict):
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)  # обрабатываем ключи
            total_sum += calculate_structure_sum(value)  # обрабатываем значения

    return total_sum

print(calculate_structure_sum(data_structure))
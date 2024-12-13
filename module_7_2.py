def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            position = file.tell()  # Получаем текущую позицию в файле
            file.write(string + '\n')  # Записываем строку с переводом строки
            strings_positions[(line_number, position)] = string  # Добавляем в словарь

    return strings_positions

info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

    ]

result = custom_write('test.txt', info)

# print(result.items())
for elem in result.items():

  print(elem)
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__set_vin(vin)
        self.__set_numbers(numbers)

    def __set_vin(self, vin):
        if self.__is_valid_vin(vin):
            self.__vin = vin

    def __set_numbers(self, numbers):
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        # Нужно принимать номер VIN как строку, чтобы, если вдруг среди цифр случайно введут букву или другой символ,
        # чтобы иметь возможность корректно обработать эту ошибку
        try:
            vin_number = int(vin_number)  # Попытка преобразования в число
        except ValueError:
            raise IncorrectVinNumber('VIN должен содержать только цифры')

        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для VIN номера')
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        # Помимо длины номера нужно ещё проверять, из каких именно символов состоит номер.
        # Иначе могут появиться номера типа "ТР2И64" или "отдури"
        if not (numbers[0].isalpha() and numbers[1:4].isdigit() and numbers[4:].isalpha()):
            raise IncorrectCarNumbers('Некорректный формат номера')
        return True


try:
    first = Car('Model1', '1000000', 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', '300', 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', '202y202', 'A032BC')  # Ошибочный VIN с буквой
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

try:
    fourth = Car('Model3', '2020202', 'CDR257')  # Ошибочный номер
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{fourth.model} успешно создан')

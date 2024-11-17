class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        # print(args)
        # print(kwargs)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

# перегрузка операторов
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors == other
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors < other
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors <= other
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors > other
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors >= other
        return False

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
    
    # увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return NotImplemented
    
    # работают так же как и __add__(возвращают результат его вызова).
    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    # Метод для вычитания ( - )
    def __sub__(self, other):
        if isinstance(other, int):
            self.number_of_floors -= other
            return self
        if isinstance(other, House):
            self.number_of_floors -= other.number_of_floors
            return self
        return NotImplemented

    # Метод для умножения ( * )
    def __mul__(self, other):
        if isinstance(other, int):
            self.number_of_floors *= other
            return self
        return NotImplemented

    # Метод для деления ( / )
    def __truediv__(self, other):
        if isinstance(other, int):
            if other == 0:
                print("Деление на ноль невозможно")
            self.number_of_floors //= other
            return self
        return NotImplemented

    # Метод для возведения в степень ( ** )
    def __pow__(self, other):
        if isinstance (other, int):
            self.number_of_floors **= other
            return self
        return NotImplemented
        # pass


    def go_to(self, new_floor):  # new_floor - номер этажа, на который нужно приехать
        # print (new_floor > self.number_of_floors)
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа нет в этом доме.')
        else:
            for i in range(1, new_floor + 1):
                print(f'{i}-й этаж')

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории...')

hr = House('"Хрущоба"', 5)
print(House.houses_history)
Dubai = House('"Бурдж-Халифа"', 163)
print(House.houses_history)
townhouse = House('"Частник"', 2)
print(House.houses_history)
print(hr.name + ',', hr.number_of_floors, 'этажей.')
print(Dubai.name + ',', Dubai.number_of_floors, 'этажа.')

print(hr)
print(Dubai)
print(townhouse)

del townhouse

print(f'"Длина" "Хрущобы" {len(hr)} этажей')
print(f'"Длина" {Dubai.name} {len(Dubai)} этажа')

hr.go_to(3)
hr.go_to(8)
Dubai.go_to(6)
Dubai.go_to(-1)

print(hr > Dubai)
print(hr >= Dubai)
print(hr < Dubai)
print(hr <= Dubai)
print(hr == Dubai)
print(hr != Dubai)

hr = hr + 10 # __add__
print(hr)

hr += 10 # __iadd__
print(hr)

Dubai = 10 + Dubai # __radd__
print(Dubai)

hr = hr / -2
print(hr)

Dubai = Dubai - 54 # __radd__
print(Dubai)
import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.filled = False

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        return (all(isinstance(side, int) and side > 0 for side in new_sides)
                and len(new_sides) == self.sides_count)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        return self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        sides = self.get_sides()
        p = sum(sides) / 2  # Полупериметр
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))
        print(p)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = [1]
        super().__init__(color, *sides * self.sides_count)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3


# Проверка работы классов
circle1 = Circle((200, 200, 100), 10)  # Цвет, сторона
print(f'Цвет круга {circle1.get_color()}')

triangle1 = Triangle((38, 78, 27), 12,17,22)
print(f'Цвет треугольника {triangle1.get_color()}')
print(f'Стороны треугольника {triangle1.get_sides()}')
print(f'Площадь треугольника {triangle1.get_square()}')

cube1 = Cube((222, 35, 130), 9)

# Проверка изменения цвета
circle1.set_color(55, 66, 77)  # Изменится
print(f'Цвет круга {circle1.get_color()}')

print(f'Цвет треугольника {triangle1.get_color()}')

cube1.set_color(300, 70, 15)  # Не изменится
print(f'Цвет куба {cube1.get_color()}')

# Проверка изменения сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (длины окружности круга)
print(f'Длина окружности {len(circle1)}')

# Проверка объёма куба
print(f'Объём куба {cube1.get_volume()}')

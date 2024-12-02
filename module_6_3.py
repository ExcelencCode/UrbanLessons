import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _coords = [0, 0, 0]

    def __init__(self, speed):
        self.speed = speed
        pass

    def move(self, dx, dy, dz):
        self._coords[0] += dx * self.speed
        self._coords[1] += dy * self.speed
        if self._coords[2] + dz * self.speed < 0:
            print("Слишком глубоко, я не умею нырять :(")
        else:
            self._coords[2] += dz * self.speed
        pass

    def get_coords(self):
        x, y, z = self._coords
        print(f"X: {x}, Y: {y}, Z: {z}")
        pass

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Не волнуйтесь, я мирный :)")
        else:
            print("Берегись, я атакую! 0_o")

    def speak(self):
        print(self.sound)


class Bird(Animal):

    beak = True

    # Выводим количество яиц
    def lay_eggs(self):
        eggs = random.randint(1, 4)
        if eggs == 1:
            print(f"Вот {eggs} яичко для Вас")
        else: print(f"Вот {eggs} яичка для Вас")


class AquaticAnimal(Animal):

    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        # Ныряние, уменьшение координаты Z
        dz = abs(dz) # Берем значение по модулю
        self.speed /= 2  # Скорость при нырянии уменьшается в два раза
        self.move(0, 0, -dz)  # Двигаемся только по оси Z


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


# Класс Duckbill, множественное наследование
class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"  # Утконос издает этот звук

    def __init__(self, speed):
        # Инициализируем с помощью конструктора родительских классов
        super().__init__(speed)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()

db.attack()

db.move(1, 2, 3)

db.get_coords()

db.dive_in(6)

db.get_coords()

db.lay_eggs()

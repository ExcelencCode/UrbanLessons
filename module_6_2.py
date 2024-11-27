class Vehicle:
    __COLOR_VARIANTS = ['зелёный', 'оранжевый', 'жёлтый', 'синий', 'красный']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self,new_color):
        if any(new_color.lower() == item.lower() for item in Vehicle.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f'Нельзя поменять цвет на {new_color}')


class Sedan(Vehicle):
       __PASSENGERS_LIMIT = 5

bibi1 = Sedan('Fifa', 'Cadillac', 'красный', 350)
bibi1.print_info()

bibi1.set_color('оранжевый')
bibi1.set_color('чёрный')
bibi1.owner = 'Перекуп'
bibi1.print_info()
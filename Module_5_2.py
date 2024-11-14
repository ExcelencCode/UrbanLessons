class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def go_to(self, new_floor): # new_floor - номер этажа, на который нужно приехать
        # print (new_floor > self.number_of_floors)
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа нет в этом доме.')
        else:
            for i in range (1, new_floor+1):
                print(f'{i}-й этаж')

    def __del__(self):
        print(f'{self.name} сломался...')

shpak = House ('"Скворечник"', 5)
Dubai = House ('"Бурдж-Халифа"', 163)
print(shpak.name + ',', shpak.number_of_floors, 'этажей.')
print(Dubai.name + ',', Dubai.number_of_floors, 'этажа.')

print(shpak)
print(Dubai)

print(f'"Длина" "Скворечника" {len(shpak)} этажей')
print(f'"Длина" {Dubai.name} {len(Dubai)} этажа')

shpak.go_to(3)
shpak.go_to(8)
Dubai.go_to(24)
Dubai.go_to(-1)

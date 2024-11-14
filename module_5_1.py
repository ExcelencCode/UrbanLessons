class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor): # new_floor - номер этажа, на который нужно приехать
        # print (new_floor > self.number_of_floors)
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа нет в этом доме.')
        else:
            for i in range (1, new_floor+1):
                print(i)

shpak = House ('"Скворечник"', 18)
print(shpak.name + ',', shpak.number_of_floors, 'этажей.')

shpak.go_to(3)
shpak.go_to(24)

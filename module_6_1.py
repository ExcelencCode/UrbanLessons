class Animal:

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Mammal(Animal):

    pass


class Predator(Animal):

    pass


class Plant():

    def __init__(self, name):
        self.name = name
        self.edible = False
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self,name):
        Plant.__init__(self, name)
        self.edible = True

a1 = Mammal('обезьян')
a2 = Predator('тигр')

pl1 = Flower('ромашишка')
pl2 = Fruit('банан')

print(a1.name)
print(a2.name)
print(pl1.name)
print(pl2.name)

a2.eat(pl1)
print(a2.alive)
print(a2.fed)

a1.eat(pl2)
print(a1.alive)
print(a1.fed)


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = "products.txt"

    def __init__(self):
        # Создаём файл, если его нет
        open(self.__file_name, "a").close()

    def get_products(self):
        """Считывает все товары из файла и возвращает строку"""
        with open(self.__file_name, "r") as file:
            return file.read()

    def add(self, *products):
        """Добавляет в файл __file_name продукты, если их там ещё нет."""
        existing_products = set()
        with open(self.__file_name, 'r') as file:
            for line in file:
                name = line.split(", ")[0]
                existing_products.add(name)

        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name in existing_products:
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    file.write(f'{product}\n')
                    existing_products.add(product.name) # и вот это позволяет избежать появления дублей продуктов

# Создаем файл магазина
s1 = Shop()
# Создаём несколько продуктов (из примера!)
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 3.5, 'Vegetables')
p4 = Product('Pears', 22.68, 'Fruits')

print(p2)  # Проверка __str__

s1.add(p1, p2, p3, p4) # Добавление продуктов

print(s1.get_products())  # Вывод всех продуктов

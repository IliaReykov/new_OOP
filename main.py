from abc import ABC, abstractmethod


class User_Exception(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else ('Ошибка')

    def evaluate(self):
        pass


class User_Exception_Zero_Am(User_Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Не указано количество товара'


class Base_Product:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_product(cls):
        return cls


class PrintMixin:

    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'{k}: {v},'
        return f"создан объект со свойствами {object_attributes})"


class Product(Base_Product, PrintMixin):
    name: str
    description: str
    prod: list
    price = float
    amount = int

    def __init__(self, name, description, price, amount):
        super().__init__()
        self.name = name
        self.description = description
        self.__price = price
        self.amount = amount

        if not amount or amount == 0:
            raise User_Exception_Zero_Am
        else:
            pass

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print('Цена введена некорректная')
        else:
            self.__price = value

    def __str__(self):
        return f'Название продукта: {self.name}, Цена: {self.__price}руб. Остаток: {self.amount}шт.'

    def __add__(self, other):
        return (self.__price * self.amount) + (other.price * other.amount)

    def __len__(self):
        return sum(product.prod for product in self.__prod)
        raise TypeError


class Phone(Product, PrintMixin):
    perfomance: int
    model: str
    storage: int
    color_phone: str

    @property
    def price(self):
        return self.__price

    def __add__(self, other):
        if type(self) == type(other):
            return (self.__price * self.amount) + (other.price * other.amount)
        raise ValueError("Можно складывать только экземпляры этого класса")

    def __init__(self, name, description, price, amount, perfomance, model, storage, color_phone):
        super().__init__(name, description, price, amount)
        self.perfomance = perfomance
        self.model = model
        self.storage = storage
        self.color_phone = color_phone


class Grass(Product, PrintMixin):
    made_in: str
    growth_time: int
    color_grass: str

    def __init__(self, name, description, price, amount, made_in, growth_time, color_grass):
        super().__init__(name, description, price, amount)
        self.made_in = made_in
        self.growth_time = growth_time
        self.color_grass = color_grass


if __name__ == "__main__":
    phone_1 = Phone("GoodPhone", "Smartphone", 12599, 12, 43000, 40, 16, "Ocean Blue")
    print(phone_1.__dict__)
    phone_2 = Phone("WellPhone", "Smartphone", 21999, 40, 99999, 7, 256, "Gold Star")
    print(phone_2.__dict__)
    grass_1 = Grass("Sweden Grass", "Grass", 4599, 12, "Sweden", 12, "Green")
    print(grass_1.__dict__)
    grass_2 = Grass("Australian Grass", "Grass", 1499, 40, "Australia", 36, "Yellow")
    print(grass_2.__dict__)


class Category:
    name: str
    description: str
    __products: list
    uniq_prod = 0
    num_ctg = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = []

        Category.num_ctg += 1
        Category.uniq_prod += len(self.__products)

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.uniq_prod += 1

    @property
    def products(self):
        return self.products

    @property
    def spisok_prods(self):
        left = ''
        for prod in self.products:
            left += f'{prod.name} - {prod.price}руб. Осталось: {prod.amount}\n'
        return left

    def __repr__(self):
        return f'{self.name}, {self.description}, {self.__products}'

    def __str__(self):
        return f'Название категории: {self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        amt = 0
        for product in self.__products:
            amt += product.amount
        return amt

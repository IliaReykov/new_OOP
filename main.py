class Category:
    name: str
    description: str
    prod: list

    uniq_prod = 0
    num_ctg = 0

    def __init__(self, name, description, prod):
        self.name = name
        self.description = description
        self.__prod = []

        Category.num_ctg += 1
        Category.uniq_prod += len(self.__prod)

    def add_products(self,value):
        self.__prod.append(value)
        Category.uniq_prod += 1

    @property
    def products(self):
        return self.__prod

    @property
    def spisok_prods(self):
        left = ''
        for prod in self.__prod:
            left += f'{prod.name} - {prod.price}руб. Осталось: {prod.amount}\n'
        return left

    def __repr__(self):
        return f'{self.name}, {self.description}, {self.__prod}'

    def __str__(self):
        return f'Название категории: {self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        amt = 0
        for product in self.__prod:
            amt += product.amount
        return amt

class Product:
    name: str
    description: str
    prod: list
    price = float
    amount = int

    def __init__(self, name, description, price, amount):
        self.name = name
        self.description = description
        self.price = price
        self.amount = amount

    @classmethod
    def add_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

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


product_1 = Product('Мыло', 'гигиена', 60, 8)
product_2 = Product('Губка', 'товары для кухни', 40, 12)
category_1 = Category('Хоз. товары', 'Хозяйственные товары', '')
category_2 = Category('Товары для кухни', 'Кухонные товары', '')

print(f'Название: {category_1.name}\nОписание категории: {category_1.description}\n')
print(f'Название: {category_2.name}\nОписание категории: {category_2.description}\n')
print(f'Название: {product_1.name}\nОписание товара: {product_1.description}\nЦена: {product_1.price}\nКоличесвто: {product_1.amount}\n')
print(f'Название: {product_2.name}\nОписание товара: {product_2.description}\nЦена: {product_2.price}\nКоличесвто: {product_2.amount}\n')

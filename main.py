class Category:
    name: str
    description: str
    prod: str

    def __init__(self, name, description, prod):
        self.name = name
        self.description = description
        self.prod = prod


ctgr = Category("Личная гигиена", "Предметы для личной гигены", "Мыло")
ctgr_2 = Category("Хоз. товары", "Товары для хозяйства", "Вантуз")


class Product:
    name: str
    description: str
    prod: str
    price = float
    amount = int
    categories = int
    uniq_prod = int

    def __init__(self, name, description, price, amount, categories, uniq_prod):
        self.name = name
        self.description = description
        self.price = price
        self.amount = amount
        self.categories = categories
        self.uniq_prod = uniq_prod

prdct = Product("Мыло", "Мыло - это мыло!", 10.4, 4, )


print(f'Категория товаров: {ctgr.name}')
print(f'Описание категории: {ctgr.description}')
print(f'Описание товары в категории: {ctgr.prod}')

print(f'\nКатегория товаров: {ctgr_2.name}\nОписание товары в категории: {ctgr_2.description}\nОписание товары в категории: {ctgr_2.prod}')

print(f'\nНазвание продукта: {prdct.name}\nОписание продукта: {prdct.description}\nЦена продукта: {prdct.price} Руб.\nКоличество продукта: {prdct.amount} шт.')
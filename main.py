class Category:
    name: str
    description: str
    prod: list

    uniq_prod = 0
    num_ctg = 0

    def __init__(self, name, description, prod):
        self.name = name
        self.description = description
        self.prod = prod

        Category.num_ctg += 1
        Category.uniq_prod = len(prod)


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

if __name__ == '__main__':
    prdct = Product("Мыло", "Мыло - это мыло!", 10.4, 4)
    ctgr = Category("Личная гигиена", "Предметы для личной гигены", "Мыло")
    ctgr_2 = Category("Хоз. товары", "Товары для хозяйства", "Вантуз")

    print(f'Категория товаров: {ctgr.name}')
    print(f'Описание категории: {ctgr.description}')
    print(f'Описание товары в категории: {ctgr.prod}')
    print(f'\nКатегория товаров: {ctgr_2.name}\nОписание товары в категории: {ctgr_2.description}\nОписание товары в категории: {ctgr_2.prod}')
    print(f'\nНазвание продукта: {prdct.name}\nОписание продукта: {prdct.description}\nЦена продукта: {prdct.price} Руб.\nКоличество продукта: {prdct.amount} шт.')
    print(f'\nКатегорий продуктов: {Category.num_ctg}')
    print(f'\nУникальных продуктов: {Category.uniq_prod}')

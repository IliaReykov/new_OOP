class Category:
    name: str
    description: str
    prod: str

    def __init__(self, name, description, prod):
        self.name = name
        self.description = description
        self.prod = prod
        """self.email = f"{first}.{last}@email.com"""


class Product:
    name: str
    description: str
    price: float
    amount: int


ctgr_1 = Category("Ivan", "Ivanov", 50_000)
prdct_2 = Product()
'''
emp_2.name = "Andrey"
emp_2.surname = "Ivanov"
emp_2.email = "andrey2@mai.com"
emp_2.pay = 66_666
'''

print(ctgr_1.name)
print(ctgr_1.description)
print(ctgr_1.prod)

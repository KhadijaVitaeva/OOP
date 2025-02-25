from src.abcstractProduct import AbstractProduct
from src.reprMixin import ReprMixin


class Product(ReprMixin, AbstractProduct):
    """Класс для представления товара."""

    name: str
    description: str
    __price: float
    quantity: int

    goods_created: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""

        if quantity == 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

    def __str__(self) -> str:
        return f'{self.name}, {int(self.__price)} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other) -> float:
        if not type(self) is type(other):
            raise ValueError('Складывать можно только объекты одного класса.')
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, new_product_info) -> "Product":
        # разбираем словарь на аргументы для инициализации
        name = new_product_info['name']
        description = new_product_info['description']
        price = new_product_info['price']
        quantity = new_product_info['quantity']
        color = new_product_info['color']
        # создаём и возвращаем новый продукт
        return cls(name, description, price, quantity, color)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float | int) -> None:
        """
        Устанавливает новую цену для товара, при понижении цены спрашивает подтверждение
        """
        if new_price <= 0:
            print('Введена некорректная цена')
        elif new_price < self.__price:
            confirmation = input('Вы уверены, что хотите понизить цену? y - да, n - нет')
            if confirmation == 'y':
                self.__price = new_price
        else:
            self.__price = new_price

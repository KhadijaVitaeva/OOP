from src.product_class import Product
from src.reprMixin import ReprMixin


class Category(ReprMixin):
    """Класс для представления категории."""

    name: str
    description: str
    __products: list

    # Переменная на уровне класса для подсчета количества категорий
    number_of_categories: int = 0
    # Переменная на уровне класса для подсчета количества уникальных товаров
    number_of_products: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products

        Category.number_of_categories += 1
        Category.number_of_products += len(self.__products)

    def __str__(self) -> str:
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name}, {self.description}, {self.__products})'

    def __len__(self) -> int:
        return len(self.__products)

    def add_product(self, product: Product) -> None:
        """
        Принимает объект товара и добавляет в список товаров категории, проверяя возможность добавдения
        определенного продукта в определенную категорию
        """
        if not isinstance(product, Product):
            raise TypeError('Добавлять в категорию можно только объекты класса Product.')
        self.__products.append(product)
        Category.number_of_products += 1

    @property
    def products(self) -> str:
        result = ""
        for product in self.__products:
            result += f"{str(product)}\n"
        return result

    @property
    def average_price(self) -> float:
        """
        Метод, который подсчитывает средний ценник всех товаров
        """
        summ = 0
        for product in self.products:
            summ += product.price
        try:
            average = summ / len(self.products)
            return average
        except ZeroDivisionError:
            return 0

from src.product_class import Product


class GrassLawn(Product):
    """ Дочерний класс для категории товаров 'Трава газонная' """


def __init__(self, name: str, description: str, price: float, quantity: int, color: str, country_of_prod: str,
             germination: int) -> None:
    """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""

    self.country_of_prod = country_of_prod
    self.germination = germination
    super().__init__(name, description, price, quantity, color)

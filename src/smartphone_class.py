from src.product_class import Product


class Smartphone(Product):
    """ Дочерний класс для категории товаров 'Смартфоны' """


def __init__(self, name: str, description: str, price: float, quantity: int, color: str, performance: str,
             model: str, built_in_memory: int) -> None:
    """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""

    self.performance = performance
    self.model = model
    self.built_in_memory = built_in_memory
    super().__init__(name, description, price, quantity, color)

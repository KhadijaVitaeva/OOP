from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    goods_created: list = []

    @abstractmethod
    def __init__(self):
        pass

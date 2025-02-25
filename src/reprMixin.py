class ReprMixin:
    """ Класс, выводящий сообщение о том, что объект был создан и отвечающий за repr всех дочерних объектов """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Создан объект ", repr(self))

    def __repr__(self):
        attributes = []
        for k, v in self.__dict__.items():
            string = f"{k}={v}" if type(v) != str else f"{k}='{v}'"
            attributes.append(string)
        attrs = ", ".join(attributes)
        return f'{self.__class__.__name__}({attrs})'

class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name  # Использование защищенных атрибутов
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Класс для бумажных книг. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        # Добавляем информацию о страницах
        return super().__str__() + f". Страниц: {self.pages}"

    def __repr__(self):
        # Расширяем представление с учетом страниц
        return super().__repr__()[:-1] + f", pages={self.pages})"


class AudioBook(Book):
    """ Класс для аудиокниг. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __str__(self):
        # Добавляем информацию о продолжительности
        return super().__str__() + f". Продолжительность: {self.duration: .2f} часов"

    def __repr__(self):
        # Расширяем представление с учетом продолжительности
        return super().__repr__()[:-1] + f", duration={self.duration})"

"""Код, позволяющий подсчитать размер дороги"""


from pympler import asizeof


# Вариант без уменьшения объема памяти (416 байт)
class Road:
    """Создаем класс для подсчета размера дороги"""
    def __init__(self, _length, _width, _mass):
        """Определяем параметры"""
        self._length = _length
        self._width = _width
        self._mass = _mass

    def mass_asp(self):
        """Подсчитываем"""
        return self._length * self._width * self._mass


answer = Road(100, 200, 21)
print(answer.mass_asp())
print(asizeof.asizeof(answer))


# Вариант с уменьшением объема памяти (152 байта)
# Так как мы заранее знаем кол-во атрибутов, мы можем
# сохранить их в менее затратном по памяти контейнере
class Road2:
    """Создаем класс для подсчета размера дороги"""
    __slots__ = 'length2', 'width2', 'mass2'

    def __init__(self, length2, width2, mass2):
        """Определяем параметры"""
        self.length2 = length2
        self.mass2 = mass2
        self.width2 = width2

    def mass_asp_2(self):
        """Подсчитываем"""
        return self.length2 * self.width2 * self.mass2


answer_2 = Road2(100, 200, 21)
print(answer_2.mass_asp_2())
print(asizeof.asizeof(answer_2))
"""
Liskov Substitution Principle (LSP). Принцип подстановки Барбары Лисков.

Если у вас есть API, который принимает какой-то базовый класс, то он должен корректно работать
со всеми потомками базового класса
"""


class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def __str__(self):
        return f"Width: {self._width} Height: {self._height}"

    @property
    def area(self):
        return self._height * self._width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size: int):
        super(Square, self).__init__(size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc: Rectangle):
    w = rc.width # может быть не актуальное значение width
    rc.height = 10
    expected = w * 10
    print(f"Expected area - {expected}, got {rc.area}")


if __name__ == "__main__":
    rc = Rectangle(10, 3)
    use_it(rc)

    sq = Square(5)
    use_it(sq)

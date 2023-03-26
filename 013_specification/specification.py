import abc
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    BIG = 3


class Product:
    def __init__(self, name: str, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size

    def __str__(self):
        return "<class Product> name = {}, color - {}, size - {}".format(
            self.name, self.color, self.size
        )


class Specification(abc.ABC):
    @abc.abstractmethod
    def is_satisfaction(self, item: Product):
        ...


class ColorSpecification(Specification):
    def __init__(self, color: Color):
        self.color = color

    def is_satisfaction(self, item: Product):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size: Size):
        self.size = size

    def is_satisfaction(self, item: Product):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfaction(self, item: Product):
        return all(map(lambda spec: spec.is_satisfaction(item), self.args))


class Filter(abc.ABC):
    @abc.abstractmethod
    def filter(self, items: list, spec: Specification):
        ...


class BetterFilter(Filter):
    def filter(self, items: list, spec: Specification):
        for item in items:
            if spec.is_satisfaction(item):
                yield item


if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    mellow = Product("Mellow", Color.RED, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.BIG)
    house = Product("House", Color.BLUE, Size.BIG)
    car = Product("Car", Color.RED, Size.BIG)

    products = [apple, mellow, tree, house, car]
    bf = BetterFilter()

    print("===BIG specification===")
    size_sp = SizeSpecification(size=Size.BIG)
    for product in bf.filter(products, size_sp):
        print(product)

    print("===RED specification===")
    color_sp = ColorSpecification(color=Color.RED)
    for product in bf.filter(products, color_sp):
        print(product)

    print("===AND specification===")
    cm_sp = AndSpecification(size_sp, color_sp)
    for product in bf.filter(products, cm_sp):
        print(product)

"""
Паттерн Декоратор.
Паттерн динамически наделяет объект новыми возможностями и является гибкой
альтернативой субклассированию в области расширения функциональности.
"""
import abc


class Beverage(abc.ABC):

    def __init__(self):
        self.description = "Uknown"

    def get_description(self):
        return self.description

    @abc.abstractmethod
    def cost(self): ...


class CondimentDecorator(Beverage, abc.ABC):
    @abc.abstractmethod
    def get_description(self): ...


class Espresso(Beverage):

    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "House Blend Coffee"

    def cost(self):
        return 0.89


class DarkRoast(Beverage):

    def __init__(self):
        super().__init__()
        self.description = "Dark Roast Coffee"

    def cost(self):
        return 0.99


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + 0.20


class Whip(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Whip"

    def cost(self):
        return 0.1 + self.beverage.cost()


class Soy(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return 0.15 + self.beverage.cost()


def main():
    beverage = Espresso()
    print(beverage.get_description() + f" ${beverage.cost()}")

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.get_description() + f" ${beverage2.cost()}")

    beverage3 = HouseBlend()
    beverage3 = Whip(Mocha(Soy(beverage3)))
    print(beverage3.get_description() + f" ${beverage3.cost()}")


if __name__ == "__main__":
    main()

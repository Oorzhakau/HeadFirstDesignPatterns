import abc


class PizzaIngredientFactory(abc.ABC):
    """Абстрактная фабрика для создания семейств взаимосвязанных или
    взаимозависмых объектов без указания их конкретных классов."""
    @abc.abstractmethod
    def create_dough(self): ...

    @abc.abstractmethod
    def create_sauce(self): ...

    @abc.abstractmethod
    def create_cheese(self): ...

    @abc.abstractmethod
    def create_veggies(self): ...

    @abc.abstractmethod
    def create_pepperoni(self): ...

    @abc.abstractmethod
    def create_clam(self): ...


class ThinCrustDough:
    pass


class MarinaSauce:
    pass


class ReggianoCheese:
    pass


class Garlic:
    pass


class Onion:
    pass


class RedPepper:
    pass


class Mushroom:
    pass


class SlicedPepperoni:
    pass


class FreshClamms:
    pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        return list([Garlic(), Onion(), Mushroom(), RedPepper()])

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FreshClamms()


class ThickCrustDough:
    pass


class PlumTomatoSauce:
    pass


class MozzarellaCheese:
    pass


class EggPlant:
    pass


class Spinach:
    pass


class BlackOlives:
    pass


class FrozenClamms:
    pass


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheese(self):
        return MozzarellaCheese()

    def create_veggies(self):
        return list([Spinach(), BlackOlives(), EggPlant(), PlumTomatoSauce()])

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FrozenClamms()

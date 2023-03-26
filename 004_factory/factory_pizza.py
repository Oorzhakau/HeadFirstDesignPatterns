import abc

from factory_pizza_ingredient import PizzaIngredientFactory


class Pizza(abc.ABC):

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory
        self.name: str | None = None
        self.dough: str | None = None
        self.sauce: str | None = None
        self.toppings: list = []
        self.cheese: str | None = None
        self.pepperoni: str | None = None
        self.clam: str | None = None

    @abc.abstractmethod
    def prepare(self) -> None: ...

    def bake(self) -> None:
        print("Bake for 25 min at 350 C.")

    def cut(self) -> None:
        print("Cutting the pizza into diagonal slices.")

    def box(self) -> None:
        print("Place pizza in official PizzaStore box.")

    def set_name(self, name: str = None):
        self.name = name

    def get_name(self) -> str | None:
        return self.name

    @abc.abstractmethod
    def get_description(self): ...


class CheesePizza(Pizza):
    def prepare(self) -> None:
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()

    def get_description(self):
        return "Cheese Pizza"


class VeggiePizza(Pizza):
    def prepare(self) -> None:
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()

    def get_description(self):
        return "Veggie Pizza"



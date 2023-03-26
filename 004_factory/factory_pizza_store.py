import abc

from factory_pizza import Pizza, CheesePizza, VeggiePizza
from factory_pizza_ingredient import NYPizzaIngredientFactory


class PizzaStore(abc.ABC):
    @abc.abstractmethod
    def create_pizza(self, name: str) -> Pizza:
        """Фабричный метод изолирует клиенткий код в суперклассе."""
        ...

    def order_pizza(self, name) -> Pizza:
        pizza = self.create_pizza(name=name)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class NYPizzaStore(PizzaStore):
    def create_pizza(self, name: str) -> Pizza:
        pizza = None
        factory = NYPizzaIngredientFactory()

        if name == "cheese":
            pizza = CheesePizza(factory)
            pizza.set_name("NY Cheese Pizza")
        elif name == "veggie":
            pizza = VeggiePizza(factory)
            pizza.set_name("NY Veggie Pizza")
        return pizza


if __name__ == "__main__":
    store = NYPizzaStore()
    pizza = store.order_pizza(name="cheese")
    print(pizza.get_name())
    pizza = store.order_pizza(name="veggie")
    print(pizza.get_name())

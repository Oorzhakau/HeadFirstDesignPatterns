"""
Паттерн Фабричный метод.
Фабричный метод отвечает за создание объекта и инкапсулирует эту операцию в субклассе.
"""
import abc

from factory_method_pizza import (
    ChicagoStyleCheesePizza,
    ChicagoStyleClamPizza,
    ChicagoStylePepperoniPizza,
    ChicagoStyleVeggiePizza,
    NYStyleCheesePizza,
    NYStyleClamPizza,
    NYStylePepperoniPizza,
    NYStyleVeggiePizza,
    Pizza,
)


class PizzaStore(abc.ABC):
    @abc.abstractmethod
    def create_pizza(self, name: str) -> Pizza:
        ...

    """Фабричный метод изолирует клиенткий код в суперклассе."""

    def order_pizza(self, name) -> Pizza:
        pizza = self.create_pizza(name=name)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class NYPizzaStore(PizzaStore):
    mapper = {
        "cheese": NYStyleCheesePizza,
        "pepperoni": NYStylePepperoniPizza,
        "clam": NYStyleClamPizza,
        "veggie": NYStyleVeggiePizza,
    }

    def create_pizza(self, name: str) -> Pizza:
        if name not in self.mapper:
            raise KeyError("Нет такой пиццы!")
        return self.mapper[name]()


class ChicagoPizzaStore(PizzaStore):
    mapper = {
        "cheese": ChicagoStyleCheesePizza,
        "pepperoni": ChicagoStylePepperoniPizza,
        "clam": ChicagoStyleClamPizza,
        "veggie": ChicagoStyleVeggiePizza,
    }

    def create_pizza(self, name: str) -> Pizza:
        if name not in self.mapper:
            raise KeyError("Нет такой пиццы!")
        return self.mapper[name]()


if __name__ == "__main__":
    print("Chicago store")
    chicago_store = ChicagoPizzaStore()
    pizza = chicago_store.order_pizza(name="cheese")
    print(pizza)
    print("NY store")
    ny_store = NYPizzaStore()
    pizza = ny_store.order_pizza(name="cheese")
    print(pizza)


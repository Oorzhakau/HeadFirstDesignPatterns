class Pizza:
    name: str = None
    dough: str = None
    sauce: str = None
    toppings: list = []

    def prepare(self) -> None:
        print(f"Preparing {self.name}.")
        print(f"Tossing ...")
        print(f"Adding sauce ...")
        print(f"Adding toppings {', '.join(self.toppings)}.")

    def bake(self) -> None:
        print("Bake for 25 min at 350 C.")

    def cut(self) -> None:
        print("Cutting the pizza into diagonal slices.")

    def box(self) -> None:
        print("Place pizza in official PizzaStore box.")

    def get_name(self) -> str | None:
        return self.name


class NYStyleCheesePizza(Pizza):
    name = "NY Style Deep Dish Cheese Pizza"
    dough = "This Crust Dough"
    sauce = "Marinara Sauce"
    toppings = ["Grated Reggiano Cheese"]


class NYStylePepperoniPizza(Pizza): ...


class NYStyleClamPizza(Pizza): ...


class NYStyleVeggiePizza(Pizza): ...


class ChicagoStyleCheesePizza(Pizza):
    name = "Chicago Style Deep Dish Cheese Pizza"
    dough = "Extra Thick Crust Dough"
    sauce = "Plum Tomato Sauce"
    toppings = ["Shredded Mozzarella Cheese"]

    def cut(self):
        print("Cutting the pizza into square slices.")


class ChicagoStylePepperoniPizza(Pizza): ...


class ChicagoStyleClamPizza(Pizza): ...


class ChicagoStyleVeggiePizza(Pizza): ...

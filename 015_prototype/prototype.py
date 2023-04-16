"""
Шаблон Прототип (Prototype).
Берем частично или полностью инициализированный объект и делаем глубокое его копирование.
Позволяем пользователям настраивать создаваемй объект.
"""
import copy


class Address:
    def __init__(self, street: str, city: str, country: str):
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.country} {self.city} {self.street}"


class Person:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = copy.deepcopy(address)

    def __str__(self):
        return f"{self.name} stay in address {self.address}"


if __name__ == "__main__":
    address = Address("123 London Road", "London", "UK")
    john = Person("John", address)
    print(john)
    jane = Person("Jane", address)
    print(jane)
    jane.address.street = "Ivanova 12"
    print(john)
    print(jane)

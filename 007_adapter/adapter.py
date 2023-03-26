"""
Паттерн Адаптер.
Паттерн преобразует один интерфейс в другой.
"""
import random

from duck import Duck, MallardDuck
from turkey import Turkey, BaseTurkey


class TurkeyAdapter(Duck):
    def __init__(self, turkey_obj: Turkey):
        self.turkey = turkey_obj
        self.random = random.choice([i for i in range(5)])

    def get_fly(self):
        for i in range(self.random):
            self.turkey.get_fly()

    def get_quack(self):
        self.turkey.get_gobble()


if __name__ == "__main__":
    mallard_duck = MallardDuck()
    turkey = BaseTurkey()
    turkey_adapter = TurkeyAdapter(turkey)
    for bird in [mallard_duck, turkey_adapter]:
        bird.get_fly()
        bird.get_quack()

import abc
from typing import Optional


class FlyBehavior(abc.ABC):
    """Паттерн для интерфейса полета."""
    @abc.abstractmethod
    def fly(self): ...


class QuackBehavior(abc.ABC):
    """Паттерн для интерфейса кряканья."""
    @abc.abstractmethod
    def quack(self): ...


class Duck:
    fly_instance: FlyBehavior = None
    quack_instance: QuackBehavior = None

    def get_fly(self):
        if not self.fly_instance:
            raise "FlyBehavior is not determine!"
        return self.fly_instance.fly()

    def get_quack(self):
        if not self.quack_instance:
            raise "QuackBehavior is not determine!"
        return self.quack_instance.quack()


class SpecialFly(FlyBehavior):
    def fly(self):
        return "special flying!!!"


class MallardFly(FlyBehavior):
    def fly(self):
        print("real flying!!!")


class SpecialQuack(QuackBehavior):
    def quack(self):
        print("special quack!!!")


class MallardQuack(QuackBehavior):
    def quack(self):
        print("real quack!!!")


class SpecialDuck(Duck):
    fly_instance = SpecialFly()
    quack_instance = SpecialQuack()


class MallardDuck(Duck):
    fly_instance = MallardFly()
    quack_instance = MallardQuack()


if __name__ == "__main__":
    special_duck = SpecialDuck()
    print("====SPECIAL DUCK=====")
    print(special_duck.get_fly())
    print(special_duck.get_quack())
    real_duck = MallardDuck()
    print("====MALLARD DUCK=====")
    print(real_duck.get_fly())
    print(real_duck.get_quack())
    print("====SPECIAL DUCK=====")
    print(special_duck.get_fly())
    print(special_duck.get_quack())

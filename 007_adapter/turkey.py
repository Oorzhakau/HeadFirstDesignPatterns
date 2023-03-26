import abc

from duck import FlyBehavior, MallardFly


class GobbleBehavior(abc.ABC):
    @abc.abstractmethod
    def gobble(self): ...


class TurkeyGobble(GobbleBehavior):
    def gobble(self):
        print("Gobble gobble!")


class TurkeyFly(FlyBehavior):
    def fly(self):
        print("I'm flying a short distance.")


class Turkey:
    fly_instance: FlyBehavior | None = None
    gobble_instance: GobbleBehavior | None = None

    def get_fly(self):
        if not self.fly_instance:
            raise "FlyBehavior is not determine!"
        return self.fly_instance.fly()

    def get_gobble(self):
        if not self.fly_instance:
            raise "GobbleBehavior is not determine!"
        return self.gobble_instance.gobble()


class BaseTurkey(Turkey):
    fly_instance = TurkeyFly()
    gobble_instance = TurkeyGobble()


class MixinTurkey(Turkey):
    fly_instance = MallardFly()
    gobble_instance = TurkeyGobble()


if __name__ == "__main__":
    base_turkey = BaseTurkey()
    base_turkey.get_fly()
    base_turkey.get_gobble()
    mixin_turkey = MixinTurkey()
    mixin_turkey.get_fly()
    mixin_turkey.get_gobble()
    base_turkey.get_fly()

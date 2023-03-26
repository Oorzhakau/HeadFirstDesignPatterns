import abc


class QuackBehavior(abc.ABC):
    @abc.abstractmethod
    def quack(self): ...


class MallardDuck(QuackBehavior):
    def quack(self):
        return "Quack!!!"


class ReadheadDuck(QuackBehavior):
    def quack(self):
        return "Quack!!!"


class DuckCall(QuackBehavior):
    def quack(self):
        return "Kwak!!!"


class RubberDuck(QuackBehavior):
    def quack(self):
        return "Squeak!!!"


class Goose:
    @staticmethod
    def honk():
        return "Hock!"


class GooseAdapter(QuackBehavior):
    goose = Goose()

    def quack(self):
        return self.goose.honk()


class QuackCounter(QuackBehavior):
    number_of_quacks = 0

    def __init__(self, duck: QuackBehavior):
        self.duck = duck

    def quack(self):
        QuackCounter.number_of_quacks += 1
        return self.duck.quack()

    def get_counts(self):
        return self.number_of_quacks


class DuckFactory(abc.ABC):
    @abc.abstractmethod
    def create_mallard_duck(self): ...

    @abc.abstractmethod
    def create_read_head_duck(self): ...

    @abc.abstractmethod
    def create_duck_call(self): ...

    @abc.abstractmethod
    def create_rubber_duck(self): ...

    @abc.abstractmethod
    def create_goose_adapter_duck(self): ...


class CountingDuckFactory(DuckFactory):
    def create_mallard_duck(self):
        return QuackCounter(MallardDuck())

    def create_read_head_duck(self):
        return QuackCounter(ReadheadDuck())

    def create_duck_call(self):
        return QuackCounter(DuckCall())

    def create_rubber_duck(self):
        return QuackCounter(RubberDuck())

    def create_goose_adapter_duck(self):
        return QuackCounter(GooseAdapter())


class Flock(QuackBehavior):
    def __init__(self):
        self.quackers = []

    def add(self, duck: QuackBehavior):
        if isinstance(duck, Flock):
            self.quackers.extend(duck.quackers)
        else:
            self.quackers.append(duck)

    def quack(self):
        for quacker in self.quackers:
            print(quacker.quack())


class DuckSimulator:
    def __init__(self, factory: DuckFactory):
        self.mallard_duck = factory.create_mallard_duck()
        self.read_head_duck = factory.create_read_head_duck()
        self.duck_call = factory.create_duck_call()
        self.rubber_duck = factory.create_rubber_duck()
        self.goose_duck = factory.create_goose_adapter_duck()

        self.flock = Flock()
        self.flock.add(self.mallard_duck)
        self.flock.add(self.read_head_duck)
        self.flock.add(self.duck_call)

        self.flock_with_mallards = Flock()
        self.flock_with_mallards.add(factory.create_mallard_duck())
        self.flock_with_mallards.add(factory.create_mallard_duck())
        self.flock_with_mallards.add(factory.create_mallard_duck())
        self.flock_with_mallards.add(factory.create_mallard_duck())

        self.flock.add(self.flock_with_mallards)

        self.flock.quack()


    @staticmethod
    def simulate(duck: QuackBehavior | Flock):
        print(duck.quack())

    def print_count(self):
        print(self.mallard_duck.get_counts())


if __name__ == "__main__":
    simulator = DuckSimulator(CountingDuckFactory())
    simulator.print_count()

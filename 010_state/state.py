import abc


class State(abc.ABC):
    @abc.abstractmethod
    def insert_quarter(self): ...

    @abc.abstractmethod
    def eject_quarter(self): ...

    @abc.abstractmethod
    def turn_crank(self): ...

    @abc.abstractmethod
    def dispense(self): ...

    @abc.abstractmethod
    def refill(self): ...


class ObjectWithState(abc.ABC):
    @abc.abstractmethod
    def set_state(self, state: State): ...

    @abc.abstractmethod
    def insert_quarter(self): ...

    @abc.abstractmethod
    def eject_quarter(self): ...

    @abc.abstractmethod
    def turn_crank(self): ...

    @abc.abstractmethod
    def release_ball(self): ...

    @abc.abstractmethod
    def refill(self, count): ...

    @abc.abstractmethod
    def get_no_quarter_state(self): ...

    @abc.abstractmethod
    def get_sold_out_state(self): ...

    @abc.abstractmethod
    def get_has_quarter_state(self): ...

    @abc.abstractmethod
    def get_sold_state(self): ...

    @abc.abstractmethod
    def get_count(self): ...


class NoQuarterState(State):
    def __init__(self, gumball_machine: ObjectWithState) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You inserted a quarter")
        self.gumball_machine.set_state(self.gumball_machine.get_has_quarter_state())

    def eject_quarter(self):
        print("You haven't inserted a quarter")

    def turn_crank(self):
        print("You turned, but there's no quarter")

    def dispense(self):
        print("You need to pay first")

    def refill(self):
        raise NotImplementedError

    def __str__(self):
        return "waiting for quarter"


class SoldOutState(State):
    def __init__(self, gumball_machine: ObjectWithState) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can't insert a quarter, the machine is sold out")

    def eject_quarter(self):
        print("You can't eject, you haven't inserted a quarter yet")

    def turn_crank(self):
        print("You turned, but there are no gumballs")

    def dispense(self):
        print("No gumball dispensed")

    def refill(self):
        self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())

    def __str__(self):
        return "sold out"


class HasQuarterState(State):
    def __init__(self, gumball_machine: ObjectWithState) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can't insert another quarter")

    def eject_quarter(self):
        print("Quarter returned")
        self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())

    def turn_crank(self):
        print("You turned...")
        self.gumball_machine.set_state(self.gumball_machine.get_sold_state())

    def dispense(self):
        print("No gumball dispensed")

    def refill(self):
        raise NotImplementedError

    def __str__(self):
        return "waiting for turn of crank"


class SoldState(State):
    def __init__(self, gumball_machine: ObjectWithState) -> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("Please wait, we're already giving you a gumball")

    def eject_quarter(self):
        print("Sorry, you already turned the crank")

    def turn_crank(self):
        print("Turning twice doesn't get you another gumball!")

    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.get_count() > 0:
            self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())
        else:
            self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())

    def refill(self):
        raise NotImplementedError

    def __str__(self):
        return "dispensing a gumball"


class GumballMachine(ObjectWithState):
    def __init__(self, number_gumballs) -> None:
        self.no_quarter_state = NoQuarterState(self)
        self.sold_out_state = SoldOutState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)
        self.count = number_gumballs
        if number_gumballs > 0:
            self.state = self.no_quarter_state
        else:
            self.state = self.sold_out_state

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def release_ball(self):
        print("A gumball comes rolling out the slot...")
        if self.count > 0:
            self.count -= 1

    def refill(self, count):
        self.count += count
        print(f"The gumball machine was just refilled; its new count is: {self.count}")
        self.state.refill()

    def set_state(self, state):
        self.state = state

    def get_no_quarter_state(self):
        return self.no_quarter_state

    def get_sold_out_state(self):
        return self.sold_out_state

    def get_has_quarter_state(self):
        return self.sold_out_state

    def get_sold_state(self):
        return self.sold_state

    def get_count(self):
        return self.count

    def __str__(self) -> str:
        result = []
        result.append("\nMighty Gumball, Inc.")
        result.append("\nJava-enabled Standing Gumball Model #2004")
        result.append(f"\nInventory: {self.count} gumball")
        if self.count != 1:
            result.append("s")

        result.append("\n")
        result.append(f"Machine is {self.state}\n")
        return "".join(result)


def gumball_machine_test_drive():
    gumball_machine = GumballMachine(2)
    print(gumball_machine)
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    gumball_machine.refill(5)
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print(gumball_machine)


if __name__ == "__main__":
    gumball_machine_test_drive()

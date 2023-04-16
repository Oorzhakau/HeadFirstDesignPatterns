import abc
import unittest
from enum import Enum, auto


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, balance = {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount >= self.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrew {amount}, balance = {self.balance}")
            return True
        return False

    def __str__(self):
        return f"balance = {self.balance}"


class Command(abc.ABC):
    def __init__(self):
        self.success = False

    @abc.abstractmethod
    def invoke(self):
        ...

    @abc.abstractmethod
    def undo(self):
        ...


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = auto()
        WITHDRAW = auto()

    def __init__(self, account: BankAccount, action: Action, amount: int):
        super(BankAccountCommand, self).__init__()
        self.amount = amount
        self.action = action
        self.account = account

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return

        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


class CompositeBankAccountCommand(Command, list):
    def __init__(self, items=None):
        super(CompositeBankAccountCommand, self).__init__()
        if items is None:
            items = []
        for i in items:
            self.append(i)

    def invoke(self):
        for x in self:
            x.invoke()

    def undo(self):
        for x in reversed(self):
            x.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_acc: BankAccount, to_acc: BankAccount, amount: int):
        super(MoneyTransferCommand, self).__init__(
            [
                BankAccountCommand(
                    from_acc, BankAccountCommand.Action.WITHDRAW, amount
                ),
                BankAccountCommand(to_acc, BankAccountCommand.Action.DEPOSIT, amount),
            ]
        )

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False
        self.success = ok


class TestSuite(unittest.TestCase):
    # def test_composite_deposit(self):
    #     ba = BankAccount()
    #     deposite_1 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
    #     deposite_2 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 50)
    #     composite = CompositeBankAccountCommand([deposite_1, deposite_2])
    #     composite.invoke()
    #     print(f"Invoke {ba}")
    #     composite.undo()
    #     print(f"Undo {ba}")
    #
    # def test_transfer_fail(self):
    #     ba_1 = BankAccount(100)
    #     ba_2 = BankAccount()
    #
    #     amount = 1000
    #     wd = BankAccountCommand(ba_1, BankAccountCommand.Action.WITHDRAW, amount)
    #     dc = BankAccountCommand(ba_2, BankAccountCommand.Action.DEPOSIT, amount)
    #     transfer = CompositeBankAccountCommand([wd, dc])
    #     transfer.invoke()
    #     print(f"ba_1: {ba_1} ba_2: {ba_2}")
    #     transfer.undo()
    #     print(f"ba_1: {ba_1} ba_2: {ba_2}")

    def test_better_transfer(self):
        ba_1 = BankAccount(100)
        ba_2 = BankAccount()

        amount = 100
        transfer = MoneyTransferCommand(ba_1, ba_2, amount)
        transfer.invoke()
        print(f"ba_1: {ba_1} ba_2: {ba_2}")
        transfer.undo()
        print(f"ba_1: {ba_1} ba_2: {ba_2}")
        print(transfer.success)


if __name__ == "__main__":
    unittest.main()

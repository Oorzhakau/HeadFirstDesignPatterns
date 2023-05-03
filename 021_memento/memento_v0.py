"""
Паттерн Хранитель (Memento).
Маркер / дескриптор, представляющий состояние системы. Позволяет вернуться к
состоянию, когда объект-снимок был сгенерирован. Иногда может напрямую раскрывать
информацию о состоянии.
"""


class Memento:
    def __init__(self, balance):
        self.balance = balance


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.changes = [Memento(self.balance)]
        self.current = 0

    def deposit(self, amount):
        self.balance += amount
        return Memento(self.balance)

    def restore(self, memento: Memento | None):
        if memento:
            self.balance = memento.balance

    def __str__(self):
        return f"Balance = {self.balance}"


if __name__ == "__main__":
    ba = BankAccount(100)
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)
    print(ba)

    ba.restore(m1)
    print(ba)
    ba.restore(m2)
    print(ba)

"""
Interface Segregation Principle (ISP). Принцип разделения интерфейсов.
"""
import abc


class MachineBadPattern(abc.ABC):
    @abc.abstractmethod
    def print(self, document): ...

    @abc.abstractmethod
    def fax(self, document): ...

    @abc.abstractmethod
    def scan(self, document): ...


class Printer(abc.ABC):
    @abc.abstractmethod
    def print(self, document): ...


class Scanner(abc.ABC):
    @abc.abstractmethod
    def scan(self, document): ...


class Photocopier(Printer, Scanner):
    def print(self, document): ...

    def scan(self, document): ...

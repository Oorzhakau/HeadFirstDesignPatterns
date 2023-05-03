"""
Паттерн Наблюдатель.
Данный паттерн определяет отношение "Один-ко-Многим" между объектами таким образом, что
при изменении состояния одного объекта (СУБЪЕКТА) происходит автоматическое оповещение и обновление всех
зависимых объектов.

Пример: Подписка на газету.
"""

import abc
from typing import Optional


class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self): ...


class Display(abc.ABC):
    @abc.abstractmethod
    def display(self): ...


class Subject(abc.ABC):
    @abc.abstractmethod
    def append_observer(self, observer: Observer): ...

    @abc.abstractmethod
    def remove_observer(self, observer: Observer): ...

    @abc.abstractmethod
    def notify_observers(self): ...


class WeatherData(Subject):
    def __init__(self,
                 temperature: Optional[int] = None,
                 humidity: Optional[float] = None,
                 pressure: Optional[float] = None):
        self._observers = []
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def append_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()

    def state_changed(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure


class CurrentConditionsDisplay(Observer, Display):
    def __init__(self, subject):
        self._temperature = None
        self._humidity = None
        self.subject = subject
        self.subject.append_observer(self)

    def __str__(self):
        return f"{self.__class__}"

    def update(self):
        self._temperature = self.subject.get_temperature()
        self._humidity = self.subject.get_humidity()
        self.display()

    def display(self):
        print(self)
        print(f"Current temperature - {self._temperature}")
        print(f"Current humidity - {self._humidity}")


class ForecastDisplay(Observer, Display):
    def __init__(self, subject: WeatherData):
        self._temperatures = []
        self._humidities = []
        self._pressures = []
        self.subject = subject
        self.subject.append_observer(self)

    def __str__(self):
        return f"{self.__class__}"

    def update(self):
        self._temperatures.append(self.subject.get_temperature())
        self._humidities.append(self.subject.get_humidity())
        self.display()

    def display(self):
        print(self)
        print(f"History temperatures - {self._temperatures}")
        print(f"History humidities - {self._humidities}")


if __name__ == "__main__":
    subject = WeatherData(temperature=33, humidity=0.75, pressure=770)

    curr_display = CurrentConditionsDisplay(subject=subject)
    fc_display = ForecastDisplay(subject=subject)
    
    subject.state_changed(temperature=25, humidity=0.22, pressure=670)
    subject.state_changed(temperature=22, humidity=0.21, pressure=654)

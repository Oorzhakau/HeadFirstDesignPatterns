"""
Шаблон Защитного Заместитель (Proxy).
"""


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Car:
    def __init__(self, driver: Driver):
        self.driver = driver

    def drive(self):
        print(f"Car is being driven by {self.driver.name}")


class CarProxy:
    def __init__(self, driver: Driver):
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
            return
        raise ValueError("Driver too young!")


if __name__ == "__main__":
    driver = Driver("John", 20)
    car = Car(driver)
    car.drive()

    driver.age = 14
    car = CarProxy(driver)
    car.drive()

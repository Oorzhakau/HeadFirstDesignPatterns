import copy


class Address:
    def __init__(self, street_address, suite, city):
        self.city = city
        self.street_address = street_address
        self.suite = suite

    def __str__(self):
        return f"{self.street_address}, Suite #{self.suite}, {self.city}"


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} works at {self.address}"


class EmployeeFactory:
    main_office_employee = Employee("", Address("123 East Dr", 0, "Saint-Petersburg"))
    aux_office_employee = Employee("", Address("124 East Dr", 0, "Saint-Petersburg"))

    @staticmethod
    def __new__employee(proto, name, suite) -> Employee:
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @classmethod
    def new_main_office_employee(cls, name, suite) -> Employee:
        return cls.__new__employee(cls.main_office_employee, name, suite)

    @classmethod
    def new_aux_office_employee(cls, name, suite) -> Employee:
        return cls.__new__employee(cls.aux_office_employee, name, suite)


if __name__ == "main":
    john = EmployeeFactory.new_aux_office_employee("John", 101)
    jane = EmployeeFactory.new_main_office_employee("Jane", 500)

    print(john)
    print(jane)

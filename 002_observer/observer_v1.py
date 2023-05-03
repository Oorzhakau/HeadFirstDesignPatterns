class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, name, address, age=0):
        super(Person, self).__init__()
        self._age = age
        self.name = name
        self.address = address

    def catch_a_cold(self):
        print(f"{self.name} catch a cold!!!")
        self.property_changed(self.name, self.address)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if self._age == value:
            return
        self._age = value
        self.property_changed("age", value)


class TrafficAuthority:
    def __init__(self, person):
        self.person = person
        person.property_changed.append(self.person_changed)

    def person_changed(self, name, value):
        if name == "age":
            if value < 16:
                print("Sorry")
            else:
                print("Okay! You can drive")
                self.person.property_changed.remove(self.person_changed)


def call_doctor(name, address):
    print(f"Call to Doctor for {name} to {address}")


if __name__ == "__main__":
    person = Person("Alex", "Lenina 21")
    person.property_changed.append(call_doctor)
    person.catch_a_cold()
    ta = TrafficAuthority(person)
    for age in range(14, 20):
        print(f"Setting age to {age}")
        person.age = age

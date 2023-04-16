class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **keargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **keargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print("Database::__init__()")


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)

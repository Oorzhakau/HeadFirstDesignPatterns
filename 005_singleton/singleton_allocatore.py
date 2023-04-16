from random import randrange as rr


class Database:
    _instance = None
    _constructor = False

    def __init__(self):
        if not self.__class__._constructor:
            print(f"Database loading...{rr(10, 100)}")
            self.__class__._constructor = True

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 is d2)

from random import randrange as rr


def singleton(class_):
    instance = None

    def get_instance(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = class_(*args, **kwargs)
        return instance

    return get_instance


@singleton
class Database:
    def __init__(self):
        print(f"Database loading...{rr(10, 100)}")


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 is d2)

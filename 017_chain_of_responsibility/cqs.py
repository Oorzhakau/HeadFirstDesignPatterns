"""
Разделение команд и запросов (CQS).
Команда - запрос на действие или изменение (например, установите значение атаки на 2)
Запрос - запрос информации без изменения чего-либо (например, получить значение атаки).

Брокер событий (event broker (observer))
"""
from enum import Enum
import abc


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, creature_name: str, what_to_query: WhatToQuery, default_value):
        self.value = default_value
        self.what_to_query = what_to_query
        self.creature_name = creature_name


class Game:
    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender, query: Query):
        self.queries(sender, query)


class CreatureModifier(abc.ABC):
    def __init__(self, game, creature):
        self.creature = creature
        self.game = game
        self.game.queries.append(self.handle)

    @abc.abstractmethod
    def handle(self, sender, query):
        ...


class DoubleAttackModified(CreatureModifier):
    def handle(self, sender, query):
        if (
            sender.name == self.creature.name
            and query.what_to_query == WhatToQuery.ATTACK
        ):
            query.value *= 2

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.queries.remove(self.handle)


class Creature:
    def __init__(self, game: Game, name, attack, defense):
        """
        Класс описывающий существо в игре.
        :param game: брокер событий
        :type game:
        :param name:
        :type name:
        :param attack:
        :type attack:
        :param defense:
        :type defense:
        """
        self.initial_defense = defense
        self.initial_attack = attack
        self.name = name
        self.game = game

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f"{self.name} {self.attack}/{self.defense}"


if __name__ == "__main__":
    game = Game()
    goblin = Creature(game, "Strong goblin", 2, 2)
    print(goblin)

    with DoubleAttackModified(game, goblin):
        print(goblin)
    print(goblin)

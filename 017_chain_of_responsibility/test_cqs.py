import sys
from abc import ABC
from enum import Enum


class Creature:
    ...


class Events(list):
    def __call__(self, sender, query):
        for item in self:
            item(sender, query)


class QueryType(Enum):
    ATTACK = 1
    DEFFENSE = 2


class Query:
    def __init__(self, sender, query_type, value):
        self.value = value
        self.sender = sender
        self.query_type = query_type


class GoblinModifier:
    def __init__(self, game):
        self.game = game
        self.game.events.append(self.handle)

    def handle(self, sender, query):
        ...


class GoblinDefenseModifier(GoblinModifier):
    def handle(self, sender, query):
        for creature in self.game.creatures:
            creature._defense += query.value


class GoblinAttackModifier(GoblinModifier):
    def handle(self, sender, query):
        for creature in self.game.creatures:
            creature._attack += query.value


class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        self.game = game
        self._attack = attack
        self._defense = defense
        GoblinDefenseModifier(game)
        self.game.update(self, Query(self, QueryType.DEFFENSE, 1))

    @property
    def attack(self):
        return self._attack

    @property
    def defense(self):
        return self._defense


class GoblinKing(Goblin):
    def __init__(self, game):
        super().__init__(game=game, attack=3, defense=3)
        GoblinAttackModifier(game)
        self.game.update(self, Query(self, QueryType.ATTACK, 1))


class Game:
    def __init__(self):
        self.creatures = []
        self.events = Events()

    def update(self, sender, query):
        self.events(sender, query)


goblins = ["g", "g", "gk"]
result = ""
for g in goblins:
    game = Game()
    goblin = None
    if g == "g":
        goblin = Goblin(game)
    else:
        goblin = GoblinKing(game)

    game.creatures.append(goblin)

    result += f"{goblin.attack} {goblin.defense} "

print(result)

from enum import Enum


class Event(list):
    """Класс событие."""

    def __call__(self, sender, query):
        for item in self:
            item(sender, query)


class ActionTypeEnum(Enum):
    UPDATE_ATTACK = 0
    UPDATE_DEFENCE = 1
    ATTACK = 2


class Game:
    """Брокер событий."""

    def __init__(self):
        self.events = Event()
        self.creatures = []

    def update(self, sender, query):
        self.events(sender, query)

    def print_creatures(self):
        print("=" * 50)
        print("In game active next creatures:")
        for creature in self.creatures:
            print(creature)

    def __str__(self):
        return "GAME ABOUT CHAINT RESPONSIBILITY"


class CreatureAction:
    def __init__(self, operation, data):
        self.operation = operation
        self.data = data


class Query:
    def __init__(self, sender: "Creature", action: CreatureAction):
        self.sender = sender
        self.action = action


class Creature:
    def __init__(self, name, attack, defence, game, hp=100):
        self.name = name
        self.attr_attack = attack
        self.attr_defence = defence
        self.game = game
        self.game.creatures.append(self)
        self.hp = hp

    def attack(self, creature_name):
        action = CreatureAction(
            ActionTypeEnum.ATTACK,
            {"name_for": creature_name, "value": self.attr_attack},
        )
        query = Query(self, action)
        self.game.update(self, query)

    def update_attack(self, new_attack_value: int):
        action = CreatureAction(
            ActionTypeEnum.UPDATE_ATTACK, {"value": new_attack_value}
        )
        query = Query(self, action)
        self.game.update(self, query)

    def __str__(self):
        return f"{self.name} [{self.hp} HP] {self.attr_attack} (ATACK) / {self.attr_defence} (DEFF)"


class ModifierCreature:
    def __init__(self, creature, game):
        self.creature = creature
        self.game = game
        self.game.events.append(self.handler)

    def handler(self, sender, query):
        ...

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.events.remove(self.handler)


class ModifierCreatureUpdateAttack(ModifierCreature):
    def handler(self, sender: Creature, query: Query):
        if (
            sender.name == self.creature.name
            and query.action.operation == ActionTypeEnum.UPDATE_ATTACK
        ):
            self.creature.attr_attack = query.action.data.get("value")
            print(
                f"Creature {self.creature.name} changed attack to {self.creature.attr_attack}"
            )


class ModifierCreatureAttack(ModifierCreature):
    def handler(self, sender: Creature, query: Query):
        if query.action.operation != ActionTypeEnum.ATTACK:
            return
        creature_for = [
            creature
            for creature in self.game.creatures
            if creature.name == query.action.data.get("name_for")
        ]
        if not creature_for:
            return
        attack = query.action.data.get("value")
        creature_for = creature_for[0]
        print(f"{sender.name} attack {creature_for.name}!")
        creature_for.hp -= attack
        if creature_for.hp <= 0:
            self.game.creatures.remove(creature_for)
            print(f"Creature {creature_for.name} dead!")
        print(sender)
        print(creature_for)


if __name__ == "__main__":
    game = Game()
    goblin = Creature("Слуга Саурона", 15, 2, game)
    print(goblin)
    aragorn = Creature("Арагорн", 50, 50, game)
    print(aragorn)
    with ModifierCreatureAttack(creature=goblin, game=game):
        goblin.attack(creature_name="Арагорн")
    ModifierCreatureUpdateAttack(creature=aragorn, game=game)
    ModifierCreatureAttack(creature=aragorn, game=game)
    aragorn.update_attack(new_attack_value=200)
    aragorn.attack("Слуга Саурона")
    game.print_creatures()

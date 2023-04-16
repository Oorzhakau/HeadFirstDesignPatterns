class Creature:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"{self.name} {self.attack} [ATT] / {self.defense} [DEFF]"


class CreatureModifier:
    def __init__(self, creature, **kwargs):
        self.creature = creature
        self.modifier_next = None

    def add_modifier(self, modifier):
        if self.modifier_next:
            self.modifier_next.add_modifier(modifier)
        else:
            self.modifier_next = modifier

    def handle(self):
        if self.modifier_next:
            self.modifier_next.handle()


class UpdateAttackModifier(CreatureModifier):
    def __init__(self, creature, **kwargs):
        self.value = kwargs.get("attack", 0)
        super().__init__(creature, **kwargs)

    def handle(self):
        self.creature.attack += self.value
        super().handle()


class UpdateDefenseModifier(CreatureModifier):
    def __init__(self, creature, **kwargs):
        self.value = kwargs.get("defense", 0)
        super().__init__(creature, **kwargs)

    def handle(self):
        self.creature.defense += self.value
        super().handle()


class UpdateNameModifier(CreatureModifier):
    def __init__(self, creature, **kwargs):
        self.value = kwargs.get("name", "")
        super().__init__(creature, **kwargs)

    def handle(self):
        name = self.value + " " + self.creature.name
        self.creature.name = name
        super().handle()


if __name__ == "__main__":
    aragorn = Creature(name="Aragorn", defense=10, attack=10)
    print(aragorn)
    root = CreatureModifier(aragorn)
    root.add_modifier(UpdateAttackModifier(aragorn, attack=20))
    root.add_modifier(UpdateDefenseModifier(aragorn, defense=5))
    root.add_modifier(UpdateNameModifier(aragorn, name="King"))
    root.handle()
    print(aragorn)

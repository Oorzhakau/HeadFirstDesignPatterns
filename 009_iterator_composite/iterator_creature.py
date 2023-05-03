class Creature:
    _strength = 0
    _agility = 1
    _intelligence = 2

    def __init__(self):
        self.stats = [10, 10, 10]

    @property
    def strength(self):
        return self.stats[Creature._strength]

    @strength.setter
    def strength(self, value):
        self.stats[Creature._strength] = value

    @property
    def agility(self):
        return self.stats[Creature._agility]

    @agility.setter
    def agility(self, value):
        self.stats[Creature._agility] = value

    @property
    def intelligence(self):
        return self.stats[Creature._intelligence]

    @intelligence.setter
    def intelligence(self, value):
        self.stats[Creature._intelligence] = value

    @property
    def sum_of_stats(self):
        return sum(self.stats)

    @property
    def max_stats(self):
        return max(self.stats)

    @property
    def avg_stats(self):
        return self.sum_of_stats / len(self.stats)

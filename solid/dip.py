"""
Dependency Inversion Principle (DIP). Принцип инверсии зависимостей.

Высокоуровневые реализации не должны зависить от низкоуровневых, вместо этого
они должны зависить от абстракций.
"""
import abc
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser(abc.ABC):
    @abc.abstractmethod
    def find_all_children_of(self, name): ...


class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    def __init__(self, browser: RelationshipBrowser):
        for p in browser.find_all_children_of("John"):
            print("John has a children have name - {}".format(p))


if __name__ == "__main__":
    parent = Person("John")
    child1 = Person("Chris")
    child2 = Person("Matt")

    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    research = Research(relationships)

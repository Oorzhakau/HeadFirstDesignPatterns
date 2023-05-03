"""
Паттерн Посредник (Mediator).
Компонент, который облегчает обмен данными между другими компонентами,
при этом они не обязательно знают друг о друге или имеют прямой (ссылочный)
доступ друг к друге.
Используется для обмена данными между разными компонентами.
"""
import typing


class Person:
    def __init__(self, name: str) -> None:
        self.name = name
        self.chat_log: list = []
        self.room: typing.Union["ChatRoom", None] = None

    def receive(self, sender: str, message: str) -> None:
        s: str = f"{sender}: {message}"
        print(f"[{self.name}'s chat session] {s}")
        self.chat_log.append(s)

    def say(self, message: str) -> None:
        self.room.broadcast(self.name, message)

    def private_message(self, who: str, message: str) -> None:
        self.room.message(self.name, who, message)


class ChatRoom:
    def __init__(self) -> None:
        self.people: list = []

    def join(self, person: "Person") -> None:
        join_msg = f"{person.name} joins the chat"
        self.broadcast("room", join_msg)
        person.room = self
        self.people.append(person)

    def broadcast(self, source: str, message: str) -> None:
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def message(self, source: str, destination: str, message: str) -> None:
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)


if __name__ == "__main__":
    room = ChatRoom()

    john = Person("John")
    jane = Person("Jane")
    room.join(john)
    room.join(jane)

    john.say("Hi room")
    jane.say("Hi John")

    simon = Person("Simon")
    room.join(simon)

    simon.say("Hi everyone")

    jane.private_message("Simon", "glad to see you")

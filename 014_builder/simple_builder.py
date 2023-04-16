"""
Паттерн Строитель (Builder).
Предоставляет API для поэтапного конструирования сложного объекта.
"""
text = "hello"
parts = ["<p>", text, "</p>"]
print("".join(parts))

words = [
    "hello",
    "world",
]
parts = ["<ul>"]

for w in words:
    parts.append(f"<li>{w}</li>")
parts.append("</ul>")
print("\n".join(parts))


class HtmlElement:
    indent_size = 2

    def __init__(self, name: str = "", text: str = "") -> None:
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent: int) -> str:
        lines = []
        i = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{self.text}")

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name: str) -> "HtmlBuilder":
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name: str) -> None:
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, child_name: str, child_text: str) -> None:
        self.__root.elements.append(HtmlElement(name=child_name, text=child_text))

    def add_child_fluent(self, child_name: str, child_text: str) -> "HtmlBuilder":
        self.__root.elements.append(HtmlElement(name=child_name, text=child_text))
        return self

    def __str__(self) -> str:
        return str(self.__root)


if __name__ == "__main__":
    builder = HtmlBuilder("ul")
    builder.add_child("li", "hello")
    builder.add_child("li", "world")
    print(builder)
    print()

    builder = HtmlBuilder("ul")
    builder.add_child_fluent("li", "hello").add_child_fluent("li", "world")
    print(builder)
    print()

    builder = HtmlElement.create("ul")
    builder.add_child_fluent("li", "hello").add_child_fluent("li", "world")
    print(builder)

"""
Прототип Мост (Bridge).
Шаблон позволяет соединять компоненты благодаря абстракциям.
Реализует механизм, отделяющий интерфейс (иерархию) от реализации (иерархии).
"""
import unittest
from abc import ABC


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "Drawing {} as lines"


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "Drawing {} as pixels"


class Shape:
    def __init__(self, render: Renderer):
        self.name = None
        self.render = render

    def __str__(self):
        return self.render.what_to_render_as.format(self.name)


class Triangle(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Triangle"


class Square(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Square"


if __name__ == "__main__":
    sq = Square(VectorRenderer())
    tr = Triangle(RasterRenderer())

    print(f"{str(sq)} {str(tr)}")

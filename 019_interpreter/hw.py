import sys
import re
from enum import Enum, auto


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        VARIABLE = auto()

    def __init__(self, _type, text):
        self.type = _type
        self.text = text


class Integer:
    def __init__(self, value):
        self.value = value


class BinaryExpression:
    class Type(Enum):
        ADDITION = auto()
        SUBTRACTION = auto()

    def __init__(self):
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        else:
            return self.left.value - self.right.value


class ExpressionProcessor:
    def __init__(self):
        self.variables = {}

    def lex(self, string):
        result = []
        i = 0
        while i < len(string):
            if string[i] == "+":
                result.append(Token(Token.Type.PLUS, string[i]))
            elif string[i] == "-":
                result.append(Token(Token.Type.MINUS, string[i]))
            elif string[i].isalpha():
                result.append(Token(Token.Type.VARIABLE, string[i]))
            else:
                digits = [string[i]]
                for j in range(i + 1, len(string)):
                    if string[j].isdigit():
                        digits.append(string[j])
                        i += 1
                    else:
                        break
                result.append(Token(Token.Type.INTEGER, "".join(digits)))
            i += 1
        return result

    def parse(self, tokens):
        result = BinaryExpression()
        have_lhs = False
        i = 0
        while i < len(tokens):
            token = tokens[i]

            if result.right and result.left:
                tmp = BinaryExpression()
                tmp.left = result
                result = tmp

            if token.type == Token.Type.INTEGER:
                integer = Integer(int(token.text))
                if not have_lhs:
                    result.left = integer
                    have_lhs = True
                else:
                    result.right = integer
            elif token.type == Token.Type.PLUS:
                result.type = BinaryExpression.Type.ADDITION
            elif token.type == Token.Type.MINUS:
                result.type = BinaryExpression.Type.SUBTRACTION
            elif token.type == Token.Type.VARIABLE:
                integer = Integer(self.variables[token.text])
                if not have_lhs:
                    result.left = integer
                    have_lhs = True
                else:
                    result.right = integer
            i += 1
        return result

    def calculate(self, expression):
        try:
            tokens = self.lex(expression)
            parsed = self.parse(tokens)
            if not parsed.type:
                return parsed.left.value if parsed.left else 0
            result = parsed.value
        except (AttributeError, KeyError):
            return 0
        else:
            return result

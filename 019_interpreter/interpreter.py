from enum import Enum, auto


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPAREN = auto()
        RPAREN = auto()

    def __init__(self, _type, text):
        self.type = _type
        self.text = text

    def __str__(self):
        return f"`{self.text}`"

    def __repr__(self):
        return f"`<class Token `{self.text}`>"


def lex(input):
    result = []

    i = 0
    while i < len(input):
        if input[i] == "+":
            result.append(Token(Token.Type.PLUS, "+"))
        elif input[i] == "-":
            result.append(Token(Token.Type.MINUS, "-"))
        elif input[i] == "(":
            result.append(Token(Token.Type.LPAREN, "("))
        elif input[i] == ")":
            result.append(Token(Token.Type.RPAREN, ")"))
        else:
            digits = [input[i]]
            for j in range(i + 1, len(input)):
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1
                else:
                    break
            result.append(Token(Token.Type.INTEGER, "".join(digits)))
        i += 1
    return result


class Integer:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"`<class Integer `{self.value}`>"


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

    def __repr__(self):
        return f"`<class BinaryExpression type={self.type} left=`{self.left} right=`{self.right}>"


def parse(tokens):
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
        elif token.type == Token.Type.LPAREN:
            j = i + 1
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j += 1
            subexpression = tokens[i + 1 : j]
            element = parse(subexpression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            i = j
        i += 1
    return result


def calc(input):
    tokens = lex(input)
    parsed = parse(tokens)
    print(f"{input}={parsed.value}")


if __name__ == "__main__":
    calc("(13+4)-(12+1)")
    calc("(1+2)-(3+4)+5")
    calc("1+(2+3)-(4+5)+6")

import sys
from copy import deepcopy


class Token:
    def __init__(self, value=0):
        self.value = value


class Memento(list):
    pass


class TokenMachine:
    def __init__(self):
        self.tokens = []

    def add_token_value(self, value):
        return self.add_token(Token(value))

    def add_token(self, token):
        if token:
            self.tokens.append(token)
            return Memento(deepcopy(self.tokens))
        return

    def revert(self, memento):
        self.tokens = memento


# tokens_str_vals = sys.stdin.read().split()
tokens_str_vals = "123:R 456".split()

tm = TokenMachine()
tokens = []
mementos = []
token_index_to_revert = -1
token_change = None
for idx, token_str_val in enumerate(tokens_str_vals):
    token_str = token_str_val.split(":")

    val = None
    if len(token_str) == 1:
        # print(token_str[0])
        val = int(token_str[0])
    else:
        # print(token_str[0])
        val = int(token_str[0])
        if token_str[1] == "R":
            token_index_to_revert = idx
        elif token_str[1][0] == "C":
            token_change = (val, int(token_str[1][1]))

    t = Token(val)
    m = tm.add_token_value(t.value)

    tokens.append(t)
    mementos.append(m)

if token_change:
    tokens[token_change[1]].value = token_change[0]

tm.revert(mementos[token_index_to_revert])

result = f"{len(tm.tokens)} "

for t in tm.tokens:
    result += str(t.value)

print(result)

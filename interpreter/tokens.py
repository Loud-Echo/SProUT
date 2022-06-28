from typing import List


class Token:
    pass


class FuncName (Token):
    def __init__(self, name: str):
        self.name = name


class Memory (Token):
    pass


class Var (Memory):
    def __init__(self, name: str):
        self.name = name


class Stack (Memory):
    def __init__(self, name: str):
        self.name = name


class Register (Memory):
    def __init__(self, name: str):
        self.name = name


class Number (Token):
    def __init__(self, val: int):
        self.val = val


class Input (Token):
    pass


class Output (Token):
    pass


class Statement (Token):
    def __init__(self, line: int, parent: Token):
        self.line = line
        self.parent = parent


class Jump (Statement):
    pass


class Shift (Statement):
    def __init__(self, line: int, parent: Token, origin: Memory | Input | Number, target: Memory | Output, funcs: List[FuncName]):
        super().__init__(line, parent)
        self.origin = origin
        self.target = target
        self.funcs = funcs


class While(Shift):
    def __init__(self, line: int, parent: Token):
        super().__init__(line, parent, Number(line), Register("jmp"), [])


class Block(Token):
    def __init__(self, content):
        self.content = content

    def set_content(self, content):
        self.content = content


class VarBlock (Token):
    def __init__(self, names: List[Var]):
        self.content = names


class Function (Block):
    def __init__(self, var_block: VarBlock, operations: List[Statement]):
        super().__init__(operations)
        self.var_block = var_block


class IfFi (Statement):
    def __init__(self, line: int, parent: Token, content: (List[Statement])):
        super().__init__(line, parent)
        self.content = content


class Elihw (IfFi):
    def __init__(self, line: int, parent: Token):
        super().__init__(line, parent, [Jump(line, self)])

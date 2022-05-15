from typing import List


class Token:
    pass


class FuncName (Token):
    def __init__(self, name: str):
        self.name = name


class Memory (Token):
    pass


class VarName (Memory):
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
    pass


class Shift (Statement):
    def __init__(self, line: int, origin: Memory | Input | Number, target: Memory | Output, funcs: List[FuncName]):
        self.line = line
        self.origin = origin
        self.target = target
        self.funcs = funcs


class Block (Statement):
    def __init__(self, content: List[Statement] | List[VarName]):
        self.content = content


class VarBlock (Block):
    def __init__(self, names: List[VarName]):
        super().__init__(names)


class Function (Block):
    def __init__(self, var_block: VarBlock, operations: List[Statement]):
        super().__init__(operations)
        self.var_block = var_block


class IfFi (Block):
    def __init__(self, content: (List[Statement])):
        super().__init__(content)

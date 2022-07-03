from typing import List

# Enthält die Klassen der geparsten Tokens (größtenteils selbsterklärend)


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

    def __str__(self):
        return f"var({self.name})"


class Stack (Memory):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"stack({self.name})"


class Register (Memory):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"reg({self.name})"


class Number (Token):
    def __init__(self, val: int):
        self.val = val

    def __str__(self):
        return f"num({self.val})"


class Input (Token):
    pass


class Output (Token):
    pass


class Statement (Token):
    def __init__(self, line: int):
        self.line = line
        self.parent = None


class Jump (Statement):
    pass


class Shift (Statement):
    def __init__(self, line: int, origin: Memory | Input | Number, target: Memory | Output,
                 funcs: List[FuncName]):
        super().__init__(line)
        self.origin = origin
        self.target = target
        self.funcs = funcs

    def __str__(self):
        return f"shift: {self.origin} {self.funcs} -> {self.target}"


class While(Shift):
    def __init__(self, line: int):
        super().__init__(line, Number(line), Register("jmp"), [])


class Block(Token):
    def __init__(self, content):
        self.content = content
        for i in range(len(content)):
            content[i].parent = self


class VarBlock (Token):
    def __init__(self, names: List[Var]):
        self.content = names


class Function (Block):
    def __init__(self, var_block: VarBlock, operations: List[Statement]):
        super().__init__(operations)
        self.var_block = var_block

    def __str__(self):
        return "-> function"


class IfFi (Statement):
    def __init__(self, line: int, content: (List[Statement])):
        super().__init__(line)
        self.content = content
        for i in range(len(content)):
            content[i].parent = self


class Elihw (IfFi):
    def __init__(self, line: int):
        super().__init__(line, [Jump(line)])

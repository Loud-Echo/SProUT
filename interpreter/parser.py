from tokens import *
from typing import List, Tuple


RESERVED = ["<", ">", "inn", "out", "tst", "jmp", "if", "fi", "while", "elihw", "jump", "var", "rav", "func", "cnuf"]


def parse_file(tokens: List[Tuple[int, str]]):
    funcs = {}
    i = 0
    while i < len(tokens):
        if tokens[i][1] == "func":
            funcs[tokens[i+1][1]], i = parse_func(i+2, tokens)
        else:
            raise(SyntaxError(f"Error in File Parsing (line #{tokens[i][0]})"))
        i += 1
    return funcs


def parse_func(i: int, tokens: List[Tuple[int, str]]) -> (Function, int):
    if tokens[i][1] != "var":
        raise (SyntaxError(f"Error in Function Parsing (line #{tokens[i][0]})"))
    i += 1
    var_names = []
    while tokens[i][1] != "rav":
        if not tokens[i][1] in RESERVED + var_names and tokens[i][1][0] != '"':
            var_names.append(tokens[i][1])
        else:
            raise (SyntaxError(f"Error in VarBlock Parsing (line #{tokens[i][0]})"))
        i += 1
    var_block = VarBlock(list(map(lambda x: Var(x), var_names)))
    i += 1

    operations, i = parse_block(i, tokens, var_block, "cnuf")

    return Function(var_block, operations), i


def parse_block(i: int, tokens: List[Tuple[int, str]], var_block: VarBlock, end_token: str) -> (List[Block | Shift], int):
    operations = []
    origins = ["<", ">", "inn", "jmp", "tst"] + list(map(lambda x: x.name, var_block.content))
    in_block = True
    while in_block:
        match tokens[i][1]:
            case e if e == end_token:
                in_block = False
            case "if":
                iffi_ops, i = parse_block(i+1, tokens, var_block, "fi")
                operations.append(IfFi(iffi_ops))
            case "jump":
                operations.append(Jump())
            case "while":
                operations.append(While(tokens[i][0]))
            case "elihw":
                operations.append(Elihw())
            case o if o in origins or o[0] == '"':
                shift, i = parse_shift(i, tokens, var_block)
                operations.append(shift)
            case _:
                raise (SyntaxError(f"Error in Block Parsing (line #{tokens[i][0]})"))
        i += 1
    return operations, i - 1


def parse_shift(i: int, tokens: List[Tuple[int, str]], var_block: VarBlock) -> (Shift, int):
    line = tokens[i][0]
    match tokens[i][1]:
        case "inn":
            orig = Input()
        case "<" | ">" as name:
            orig = Stack(name)
        case "jmp" | "tst" as name:
            orig = Register(name)
        case n if n[0] == '"':
            orig = Number(int(n[1::]))
        case name if name in list(map(lambda x: x.name, var_block.content)):
            orig = Var(name)
        case _:
            raise (SyntaxError(f"Error in Shift Parsing (line #{tokens[i][0]})"))
    funcs = []
    in_shift = True
    targ = None
    while in_shift:
        in_shift = False
        i += 1
        match tokens[i][1]:
            case "out":
                targ = Output()
            case "<" | ">" as name:
                targ = Stack(name)
            case "jmp" | "tst" as name:
                targ = Register(name)
            case name if name in list(map(lambda x: x.name, var_block.content)):
                targ = Var(name)
            case func_name:
                funcs.append(FuncName(func_name))
                in_shift = True
    assert(targ is not None)
    return Shift(line, orig, targ, funcs), i

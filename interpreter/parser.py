from tokens import *


# reservierte Tokens, welche nicht für Variablen etc. verwendet werden sollten
RESERVED = ["<", ">", "inn", "out", "tst", "jmp", "if", "fi", "while", "elihw",
            "jump", "var", "rav", "func", "cnuf", "incr", "neg", "ltz"]


def parse_file(tokens: list[tuple[int, str]]) -> dict[str, Function]:
    """
    generiert aus den Strings einer Datei ihre Funktionen
    :param tokens: einzelne Tokens (tuple([Zeile],[Token String]))
    :return: Liste der Funktionen
    """
    funcs = {}
    i = 0
    while i < len(tokens):
        if tokens[i][1] == "func":
            funcs[tokens[i+1][1]], i = parse_func(i+2, tokens)
        else:
            raise(SyntaxError(f"Error in File Parsing (line #{tokens[i][0]})"))
        i += 1
    return funcs


def parse_func(i: int, tokens: list[tuple[int, str]]) -> (Function, int):
    """
    generiert eine Funktion aus einer Menge an Tokens
    :param i: anfangspunkt innerhalb der tokens
    :param tokens: Liste der tokens
    :return: (Function-Objekt, Index des nächsten tokens)
    """
    # lesen der Var Rav Block
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
    # einlesen der Operationen
    operations, i = parse_block(i, tokens, var_block, "cnuf")
    return Function(var_block, operations), i


def parse_block(i: int, tokens: list[tuple[int, str]], var_block: VarBlock,
                end_token: str) -> (list[Block | Shift], int):
    """
    liest einen Block an Operationen ein
    :param i: anfangspunkt innerhalb der tokens
    :param tokens: Liste der tokens
    :param var_block: Variablen Namen
    :param end_token: Token, der das Ende des Blocks anzeight
    :return: (Liste an Operationen, Index des nächsten tokens)
    """
    operations = []
    # Liste der möglichen Ausgangspunkte einer Datenverschiebung
    origins = ["<", ">", "inn", "jmp", "tst"] + list(map(lambda x: x.name, var_block.content))
    in_block = True
    while in_block:
        match tokens[i][1]:  # Pattern Matching der verschiedenen Arten von Blöcken
            case e if e == end_token:
                in_block = False
            case "if":
                iffi_ops, i = parse_block(i+1, tokens, var_block, "fi")
                iffi = IfFi(tokens[i][0], iffi_ops)
                for o in range(len(iffi.content)):
                    iffi.content[o].parent = iffi
                operations.append(IfFi(tokens[i][0], iffi_ops))
            case "jump":
                operations.append(Jump(tokens[i][0]))
            case "while":
                operations.append(While(tokens[i][0]))
            case "elihw":
                operations.append(Elihw(tokens[i][0]))
            case o if o in origins or o[0] == '"':
                shift, i = parse_shift(i, tokens, var_block)
                operations.append(shift)
            case b:
                print(b)
                raise (SyntaxError(f"Error in Block Parsing (line #{tokens[i][0]})"))
        i += 1
    return operations, i - 1


def parse_shift(i: int, tokens: list[tuple[int, str]], var_block: VarBlock) -> (Shift, int):
    """
    Liest eine Verschiebung ein
    :param i: anfangspunkt innerhalb der tokens
    :param tokens: Liste der tokens
    :param var_block: Variablen Namen
    :return: (Shift-Objekt, Index des nächsten Tokens)
    """
    line = tokens[i][0]
    # Pattern matching des Ausgangspunkt
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
    # Patter matching des Ziels
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

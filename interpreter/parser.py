from tokens import *
from typing import List


def parse_file(tokens):
    funcs = {}
    i = 0
    while i < len(tokens):
        if tokens[i] == "func":
            funcs[tokens[i+1]], i = parse_func(i+2, tokens)
        else:
            raise(SyntaxError(f"Error in File Parsing (token #{i})"))
        i += 1


def parse_func(i: int, tokens: List[str]) -> (Function, int):
    return None, None  # TODO


def parse_block(i: int, tokens: List[str]) -> (Block, int):
    return None, None  # TODO


def parse_shift(i: int, tokens: List[str]) -> (Shift, int):
    return None, None  # TODO

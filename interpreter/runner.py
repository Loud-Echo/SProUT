from typing import List
import memory
import tokens


def run_func(f_string, funcs: dict[str, tokens.Function], inn: memory.Inn, out: memory.Out, left: memory.Stack,
             right: memory.Stack):
    tst = memory.FixedMem()
    jmp = memory.FixedMem()
    f = funcs[f_string]
    variables = {}
    for i in f.var_block.content:
        variables[i.name] = memory.FixedMem()
    s = f.content[0]
    running = True
    while running:
        s = run_statement(s, f.content, variables, inn, out, left, right, tst, jmp)


def run_statement(s: tokens.Statement, statements: List[tokens.Statement], variables: dict[str, memory.FixedMem],
                  inn: memory.Inn, out: memory.Out, left: memory.Stack, right: memory.Stack,
                  tst: memory.FixedMem, jmp: memory.FixedMem) -> tokens.Statement:
    match s:
        case tokens.Jump:
            for i in statements:
                if i.line == jmp.get():
                    return i
        case tokens.Shift:
            match s.origin:
                case tokens.Var:
                    orig = variables(s.origin.name)
                case tokens.Stack:
                    if s.origin.name == "<":
                        orig = left
                    if s.origin.name == ">":
                        orig = right
                case tokens.Input:
                    orig = inn
                case tokens.Output:
                    orig = out
                case tokens.Register:
                    if s.orig.name == "jmp":
                        orig = jmp
                    if s.orig.naem == "tst":
                        orig = tst
            match s.target:
                case tokens.Var:
                    targ = variables(s.origin.name)
                case tokens.Stack:
                    if s.target.name == "<":
                        targ = left
                    if s.target.name == ">":
                        targ = right
                case tokens.Input:
                    targ = inn
                case tokens.Output:
                    targ = out
                case tokens.Register:
                    if s.target.name == "jmp":
                        targ = jmp
                    if s.target.naem == "tst":
                        targ = tst
            if s.funcs:
                pass   # TODO
            else:
                targ.push(orig.get())
        case tokens.IfFi:
            pass    # fuck

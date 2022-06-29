import memory
import tokens


# TODO Basisfunktion & mehr erfinden


def run_func(f: tokens.Function, funcs: dict[str, tokens.Function],
             inn: memory.Inn, out: memory.Out,
             left: memory.Stack, right: memory.Stack):
    tst = memory.FixedMem()
    jmp = memory.FixedMem()
    variables = {}
    for i in f.var_block.content:
        variables[i.name] = memory.FixedMem()
    s = f.content[0]
    while s:
        s = run_statement(funcs, s, variables, inn, out, left, right, tst, jmp)


def pull_from_funcs(func_path: list[tokens.Function], funcs_dict, origin: memory.Memory,
                    left: memory.Stack, right: memory.Stack) -> list[int]:
    if len(func_path) == 0:
        return [origin.get()]
    f = func_path[len(func_path) - 1]
    funcs = funcs_dict
    re = []

    def pipe_inn():
        return pull_from_funcs(func_path[0:-1], funcs_dict, origin, left, right)

    def pipe_out(val):
        re.append(val)

    inn = memory.BufferedInn(pipe_inn)
    out = memory.Out(pipe_out)
    run_func(f, funcs, inn, out, left, right)
    return re


def find_line(block: tokens.Function | tokens.IfFi, line: int) -> tokens.Statement:
    content = block.content
    if content[0].line < line < content[len(content) - 1].line:
        index = binary_search(content, line)
        if content[index].line == line:
            return content[index]
        elif type(content[index] == tokens.IfFi):
            return find_line(content[index].content, line)
    elif type(block) == tokens.IfFi:
        return find_line(block.parent, line)
    raise (RuntimeError(f"couldn't find specified line ({line})"))


def binary_search(content: list[tokens.Statement], line: int):
    first = 0
    last = len(content) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if content[mid].line >= line > content[mid - 1].line:
            index = mid
        else:
            if line < content[mid].line:
                last = mid - 1
            else:
                first = mid + 1
    return index


def get_next(s: tokens. Statement) -> tokens.Statement | None:
    nex = False
    for i in s.parent.content:
        if nex:
            return i
        if i == s:
            nex = True
    if isinstance(s.parent, tokens.IfFi):
        return get_next(s.parent)
    else:
        return None


def run_statement(funcs: dict[str, tokens.Function], s: tokens.Statement, variables: dict[str, memory.FixedMem],
                  inn: memory.Inn, out: memory.Out, left: memory.Stack, right: memory.Stack,
                  tst: memory.FixedMem, jmp: memory.FixedMem) -> tokens.Statement:
    if isinstance(s, tokens.Jump):
        return find_line(s.parent.content, jmp.get())
    elif isinstance(s, (tokens.IfFi, tokens.Elihw)):
        if tst.get() == 0 or not s.content:
            return get_next(s)
        else:
            return s.content[0]
    elif isinstance(s, (tokens.Shift, tokens.Elihw)):
        targ = None
        orig = None
        if isinstance(s.origin, tokens.Var):
            orig = variables[s.origin.name]
        elif isinstance(s.origin, tokens.Stack):
            if s.origin.name == "<":
                orig = left
            if s.origin.name == ">":
                orig = right
        elif isinstance(s.origin, tokens.Register):
            if s.origin.name == "jmp":
                orig = jmp
            if s.origin.name == "tst":
                orig = tst
        elif isinstance(s.origin, tokens.Input):
            orig = inn
        elif isinstance(s.origin, tokens.Output):
            orig = out
        elif isinstance(s.origin, tokens.Number):
            orig = memory.Number(s.origin.val)

        if isinstance(s.target, tokens.Var):
            targ = variables[s.target.name]
        if isinstance(s.target, tokens.Stack):
            if s.target.name == "<":
                targ = left
            if s.target.name == ">":
                targ = right
        if isinstance(s.target, tokens.Input):
            targ = inn
        if isinstance(s.target, tokens.Output):
            targ = out
        if isinstance(s.target, tokens.Register):
            if s.target.name == "jmp":
                targ = jmp
            if s.target.name == "tst":
                targ = tst
        result = pull_from_funcs([funcs[name_obj.name] for name_obj in s.funcs], funcs, orig, left, right)
        for i in result:
            targ.push(i)
        return get_next(s)

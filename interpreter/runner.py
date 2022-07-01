import memory
import tokens


# TODO kommentare

def run_func(f: tokens.Function, funcs: dict[str, tokens.Function],
             inn: memory.Inn, out: memory.Out,
             left: memory.Stack, right: memory.Stack) -> None:
    """
    führt eine Funktion aus
    :param f: Funktion
    :param funcs: geladene Funktionen
    :param inn: Input Speicher
    :param out: Output Speicher
    :param left: linker Stack
    :param right: rechter Stack
    """
    # anlegen der lokalen Speicher
    tst = memory.FixedMem()
    jmp = memory.FixedMem()
    variables = {}
    for i in f.var_block.content:
        variables[i.name] = memory.FixedMem()
    # ausführen der Befehle
    s = f.content[0]
    while s:
        s = run_statement(funcs, s, variables, inn, out, left, right, tst, jmp)


def pull_from_funcs(func_names: list[str], funcs_dict, origin: memory.Memory,
                    left: memory.Stack, right: memory.Stack) -> list[int]:
    """
    fragt das nächste Element aus einer Funktionen-Kette an.
    :param func_names: Namen der Funktionen der Verkettung
    :param funcs_dict: geladene Funktionen
    :param origin: Ort von dem die erste Funktion ihre Daten bezieht
    :param left: linker Stack
    :param right: rechter Stack
    :return:
    """
    if len(func_names) == 0:  # falls es keine weiteren Funktionen, von denen gezogen werden kann
        return [origin.get()]
    f_name = func_names[-1]

    # eingebaute standard funktionen
    if f_name == "incr":
        return [pull_from_funcs(func_names[0:-1], funcs_dict, origin, left, right)[0] + 1]
    elif f_name == "neg":
        return [-1 * pull_from_funcs(func_names[0:-1], funcs_dict, origin, left, right)[0]]
    elif f_name == "ltz":
        return [1 if pull_from_funcs(func_names[0:-1], funcs_dict, origin, left, right)[0] < 0 else 0]

    f = funcs_dict[f_name]
    funcs = funcs_dict
    re = []

    # anlegen der Verbindungspunkte zwischen der vorherigen und folgenden Funktion
    def pipe_inn():
        return pull_from_funcs(func_names[0:-1], funcs_dict, origin, left, right)

    def pipe_out(val):
        re.append(val)

    inn = memory.BufferedInn(pipe_inn)
    out = memory.Out(pipe_out)
    run_func(f, funcs, inn, out, left, right)  # ausführen der Funktion
    return re


def find_line(block: tokens.Function | tokens.IfFi, line: int) -> tokens.Statement:
    """
    Methode zum finden einer Zeile von einem Code Block ausgehend
    :param block: Ausgangsblock
    :param line: Ziel
    :return: Statement Objekt mit der gesuchten Zeile
    """
    content = block.content
    if content[0].line <= line <= content[-1].line:
        index = binary_search(content, line)
        if content[index].line == line:
            return content[index]
        elif isinstance(block, (tokens.IfFi, tokens.Elihw)):
            return find_line(content[index].content, line)
    elif isinstance(block, (tokens.IfFi, tokens.Elihw)):
        return find_line(block.parent, line)
    raise (RuntimeError(f"Couldn't find specified line ({line})"))


def binary_search(content: list[tokens.Statement], line: int) -> int:
    """
    Binäre Suche durch Liste an Statements (basierend auf der Zeile)
    :param content: Liste der Statements
    :param line: gesuchte Zeile
    :return: Index des gesuchten Statements
    """
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
    """
    sucht das Statement, dass als nächstes ausgeführt werden soll
    :param s: ausgangs Statement
    :return: nächstes Statement (falls keine weiteren Statements: None)
    """
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
    """
    führt ein Statement aus
    :param funcs: geladene Funktionen
    :param s: auszuführendes Statement
    :param variables: initiierte Variablen
    :param inn: Input Speicher
    :param out: Output Speicher
    :param left: linker Stack
    :param right: richter Stack
    :param tst: Test Register
    :param jmp: Jump Register
    :return: nächstes auszuführende Statement
    """
    # einordnen des Statements
    if isinstance(s, tokens.Jump):
        return find_line(s.parent, jmp.get())
    elif isinstance(s, (tokens.IfFi, tokens.Elihw)):
        if tst.get() == 0 or not s.content:
            return get_next(s)
        else:
            return s.content[0]
    elif isinstance(s, (tokens.Shift, tokens.Elihw)):
        # Finden der Start und Ziel Speicher
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
        need_more_points = True
        if need_more_points:
            pass  # fuck🤡
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
        # ziehen der Daten durch die Funktionskette
        result = pull_from_funcs([name_obj.name for name_obj in s.funcs], funcs, orig, left, right)
        for i in result:
            targ.push(i)
        return get_next(s)

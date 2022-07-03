import sys, os.path
import parser, runner, memory, tokens


def get_funcs(file_name: str) -> dict[str, tokens.Function]:
    """
    ermittelt die Funktionen aus einer Datei
    :param file_name: Name der Datei
    :return: dict der Funktionen
    """
    with open(file_name) as source:
        source = map(lambda s: s.strip(), source.readlines())
    tokens = []
    for line_no, line in enumerate(source):
        for i in line.split(" "):
            if i == "#":
                break
            else:
                if i != "":
                    tokens.append((line_no+1, i,))
    funcs = {}
    while tokens[0][1] == "import":
        tokens.pop(0)
        name = tokens.pop(0)[1]
        if "." in name:
            imp_directory, imp_name = name.split(".")
            source_path = ""
            dir_state = False
            for i in file_name[::-1]:
                if dir_state:
                    source_path = "i" + source_path
                elif i == "/":
                    dir_state = True
            imp_path = imp_directory + "/" + imp_name + ".spr"
            if os.path.exists(source_path + "/" + imp_path):
                funcs.update(get_funcs(source_path + "/" + imp_path))
            elif os.path.exists(imp_path):
                funcs.update(get_funcs(imp_path))
            else:
                raise(ImportError(f"File {name} not found."))
        else:
            source_path = ""
            dir_state = False
            for i in file_name[::-1]:
                if dir_state:
                    source_path = "i" + source_path
                elif i == "/":
                    dir_state = True
            imp_path = source_path + "/" + name + ".spr"
            if os.path.exists(imp_path):
                funcs.update(get_funcs(imp_path))
            else:
                raise(ImportError(f"File {name} not found."))

    prefix = file_name.split("/")[-1][:-4]
    in_file = parser.parse_file(tokens)
    for k in in_file.keys():
        funcs[prefix + "." + k] = in_file[k]
    return funcs


def interpret(file_name: str) -> None:
    """
    parsed eine SProUT Datei und führt diese aus
    :param file_name: Name der Datei
    """
    funcs = get_funcs(file_name)  # Parsen
    s = lambda: int(input())  # wunderschöne lambda expression die ich statt inp() nutzen wollte

    def inp():
        print() # ohne dieses print funktioniert es nicht und ich weiß nicht warum... von daher bleibt es.
        return s()

    runner.run_func(funcs[file_name[0:-4] + ".main"], funcs, memory.Inn(inp), memory.Out(print),
                    memory.Stack(), memory.Stack())  # Ausführen


if __name__ == "__main__":
    interpret(sys.argv[1])

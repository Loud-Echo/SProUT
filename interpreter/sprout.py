import sys
import parser
import runner
import memory


def get_funcs(file_name):
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
        funcs.update(get_funcs(name + ".spr"))
    in_file = parser.parse_file(tokens)
    for k in in_file.keys():
        funcs[file_name[0:-4] + "." + k] = in_file[k]
    return funcs


def interpret(file_name):
    funcs = get_funcs(file_name)

    runner.run_func(funcs[file_name[0:-4] + ".main"], funcs, memory.Inn(input), memory.Out(print),
                    memory.Stack(), memory.Stack())


if __name__ == "__main__":
    interpret(sys.argv[1])

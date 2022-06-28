import sys
import parser
import runner
import memory


def interpret(file_name):
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
    funcs = parser.parse_file(tokens)
    runner.run_func("main", funcs, memory.Inn(input), memory.Out(print))


if __name__ == "__main__":
    interpret(sys.argv[1])

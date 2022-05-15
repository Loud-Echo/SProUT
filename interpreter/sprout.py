import sys
import parser


def interpret(file_name):
    with open(file_name) as source:
        source = map(lambda s: s.strip(), source.readlines())
    tokens = []
    for line in source:
        for i in line.split(" "):
            if i == "#":
                break
            else:
                tokens.append(i)
    print(tokens)
    funcs = parser.parse_file(tokens)


if __name__ == "__main__":
    interpret(sys.argv[1])

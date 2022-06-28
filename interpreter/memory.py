class DynMem:
    def get(self):
        raise(IndexError("Can't get Element"))

    def push(self, element):
        raise(IndexError("Can't push Element"))


class Stack(DynMem):
    def __init__(self):
        self.data = []

    def get(self):
        if len(self.data) != 0:
            return self.data.pop()
        else:
            raise(IndexError("Can't get Element"))

    def push(self, element):
        self.data.append(element)


class Inn(DynMem):
    def __init__(self, destination):
        self.destination = destination

    def push(self, element):
        self.destination(element)


class Out(DynMem):
    def __init__(self, source):
        self.source = source

    def get(self):
        return self.source()


class FixedMem:
    def __init__(self):
        self.val = 0

    def push(self, val):
        self.val = val

    def get(self):
        return self.val

import abc


# Diese Datei definiert die verschiedenen Arten von Speicher, welche SProUT verwendet (größtenteils selbsterklärend)


class Memory(abc.ABC):
    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def push(self, element):
        pass


class DynMem(Memory):
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
    def __init__(self, source):
        self.source = source

    def get(self):
        return self.source()


class BufferedInn(Inn):
    def __init__(self, source):
        super().__init__(source)
        self.buffer = []

    def get(self):
        if not self.buffer:
            self.buffer = self.source()
        return self.buffer.pop(0)


class Out(DynMem):
    def __init__(self, destination):
        self.destination = destination

    def push(self, element):
        self.destination(element)


class FixedMem(Memory):
    def __init__(self):
        self.val = 0

    def get(self):
        return self.val

    def push(self, val):
        self.val = val


class Number(FixedMem):
    def __init__(self, val):
        super().__init__()
        self.val = val

    def push(self, val):
        raise (IndexError("Can't push Element"))

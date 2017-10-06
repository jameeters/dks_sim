from queue import Queue

class Line:
    def __init__(self, name):
        self.name = name
        self.line = Queue()
        self.tins = []
        self.touts = []

    def push(self, person):
        self.line.put(person)

    def pop(self):
        return self.line.get()

    def empty(self):
        return self.line.empty()

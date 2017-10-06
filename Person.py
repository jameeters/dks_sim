
class Person:
    def __init__(self):
        self.wait_times  = []
        self.status = None

    def start_wait(self, name, t):
        self.status = {'location': 'name', 'tin': t, 'tout': None}

    def end_wait(self, t):
        self.status['tout'] = t
        self.status['elapsed'] = t - self.status['tin']
        self.wait_times.append(self.status)
        self.status = None
